import sys


def read_references(fname):
    with open(fname) as f:
        ret = f.read().split()
    return ret


def try_match(ref, matches):
    ret = ref[:3]
    for ch in ref[3:]:
        if ch in matches:
            ret += matches[ch]
        else:
            ret += ch
    return ret


def similarity(a, b):
    set_a = set(a)
    set_b = set(b)
    return len(set_a & set_b) / max(len(set_a), len(set_b))


def numerize(candidates, matches):
    ret = []
    for c in candidates:
        m = try_match(c, matches)
        if m[3:].isdigit():
            ret.append(m)
        else:
            print(f"Cannot numerize: {c} -> {m}")
    return ret


def closest_matches(el, candidates):
    """Levenshtein distance similarity"""
    from difflib import get_close_matches
    matches = get_close_matches(el, candidates, n=3, cutoff=0.6)
    if matches:
        return ', '.join(matches)
    else:
        return ''


matches = {'O': '0', 'I': '1', 'L': '1', 'Z': '2', 'S': '5', 'B': '8', 'g': '9', 'J': '1'}


reference_file = 'hand_pick.txt'
compare_file = 'ocr_space_ref.txt'

rf = read_references(reference_file)
cf = read_references(compare_file)

rf.sort()
cf.sort()

# Numerize candidates
candidates = [c for c in cf if not c in rf]
numerized_candidates = numerize(candidates, matches)

# Redirect REPORT to file
sys.stdout = open('comparison_report.txt', 'w')
print(f"-" * 42)
print(f"RF: {len(rf):<6} CF: {len(cf):<6} similarity: {similarity(rf, cf):.2%}")
print(f"-" * 10, f"-" * 10, f"-" * 20)

cf_plus = []
for el in rf:
    if el in cf:
        print(f"{el:<10}", f"{el:<10}")
        cf_plus.append(el)
    elif el in numerized_candidates:
        ic = numerized_candidates.index(el)
        p = candidates.pop(ic)
        pn = numerized_candidates.pop(ic)
        cf_plus.append(pn)
        print(f"{el:<10}", " "*10, f"{p}")
    else:
        p = closest_matches(el, candidates)
        print(f"{el:<10}", " "*10, f"{p}")

print(f"-" * 42)

for el in cf:
    if el not in rf:
        m = try_match(el, matches)

        if m in rf:
            print(f"{'('+m+')':<10}", f"{el:<10}")
        else:
            print(f" "*10, f"{el:<10}", f"{m:<10}")

print(f"-" * 42)
print(f"RF: {len(rf):<6} CF: {len(cf):<6} similarity: {similarity(rf, cf_plus):.2%}")
print(f"-" * 42)

print(len(candidates), "candidates could not be numerized:")