with open('test_2.txt', 'r', encoding='utf-8') as tf:
    for i in range(len(tf.readlines())):
        a = tf.readline()
        print(a)
