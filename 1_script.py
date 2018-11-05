import tensorflow as tf

x = tf.constant(35)
y = (x + 5)
z = (x * 5)

#model = tf.global_variables_initializer()

with tf.Session() as session:
#    session.run(model)
    print(session.run([y,z]))
