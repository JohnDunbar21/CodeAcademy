from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

school_a_x = create_x(2, 0.8, 1, 5)
school_b_x = create_x(2, 0.8, 2, 5)

middle_x = [(a+b)/2 for (a, b) in zip(school_a_x, school_b_x)]

plt.figure(figsize=(10, 8))
ax = plt.subplot()
ax.bar(school_a_x, middle_school_a)
ax.bar(school_b_x, middle_school_b)
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)
ax.legend(['Middle School A', 'Middle School B'])
plt.title('Test Averages on Different Units')
plt.xlabel('Unit')
plt.ylabel('Test Average')

#plt.savefig('my_side_by_side.png')

plt.show()