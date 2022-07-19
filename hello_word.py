import tensorflow as rf

def func1():
    tf.add(1,2).numpy()

def func2():
    hello = tf.constant('Hello, TensorFlow!')
    hello.numpy()

def main():
    func1()
    func2()

if __name__ == "__main__":
    main()