def solve(text: str):
    lines = text.splitlines()
    pos = 50  # initial position
    end_hits = 0
    during_hits = 0

    for line in lines:
        direction = line[0]
        step = int(line[1:])
        start = pos

        # --------------------------------------------------------------
        # 1. Solve the congruence for the first k such that:
        #    (start + k) % 100 == 0 for R
        #    (start - k) % 100 == 0 for L
        #
        # Using Euclid's division lemma on the expressions:
        #    start + k = 100q        -> k = 100q - start
        #    start - k = 100q        -> k = start - 100q
        #
        # We find the smallest positive solution k0.
        # --------------------------------------------------------------

        if direction == "R":
            if start == 0:
                k0 = 100
            else:
                k0 = 100 - start
        else:
            if start == 0:
                k0 = 100
            else:
                k0 = start

        # --------------------------------------------------------------
        # 2. Count how many integers k in [1, step] satisfy the congruence.
        #
        # All solutions are: k = k0 + 100*n  for n >= 0.
        #
        # By Euclid's lemma:
        #   k <= step  ->  k0 + 100n <= step
        #              ->  100n <= step - k0
        #              ->  n <= (step - k0) // 100
        #
        # So:
        #   if k0 > step:    no solutions
        #   otherwise:       solutions = 1 + (step - k0) // 100
        # --------------------------------------------------------------

        if k0 > step:
            hits = 0
        else:
            hits = 1 + (step - k0) // 100

        # --------------------------------------------------------------
        # 3. Update the final position
        # --------------------------------------------------------------
        sign = 1 if direction == "R" else -1
        pos = (start + sign * step) % 100

        # --------------------------------------------------------------
        # 4. Separate 'during' hits from 'end' hits
        #
        # If the rotation ends at 0, one of the hits corresponds to
        # that last click. Otherwise all hits are during.
        # --------------------------------------------------------------

        if pos == 0:
            end_hits += 1
            during_hits += hits - 1
        else:
            during_hits += hits

    return end_hits, end_hits + during_hits
