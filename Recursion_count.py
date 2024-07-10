
def isPrime(n, i, step_count):

    # Corner cases
    if n == 0 or n == 1:
        return False, step_count

    # Base cases
    if n == i:
        return True, step_count
    if n % i == 0:
        return False, step_count


    step_count += 1

    # Recursive call
    return isPrime(n, i + 1, step_count)

n = 35
i = 2
step_count = 0

is_prime, total_steps = isPrime(n, i, step_count)

if is_prime:
    print("true")
else:
    print("false")

print(f"Number of steps taken: {total_steps}")

