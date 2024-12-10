import numpy as np

task = 50
correct = 11
retro_task = 30
s = 5
n = 10000


def permutations(tasks, correct, retro_task, n):
    s_list = []
    for _ in range(n):
        tasks = np.zeros(n)
        tasks[:correct] = 1
        np.random.shuffle(tasks)

        s_new = np.sum(tasks[:retro_task])
        s_list.append(s_new)
    return np.array(s_list)


s_new_values = permutations(task, correct, retro_task, n)

p_value = np.mean(s_new_values <= s)
print(p_value)
if p_value < 0.05:
    print("Мы отвергаем нулевую гипотезу H0.")
else:
    print("Мы не можем отвергнуть нулевую гипотезу H0.")
