package datastructure.stackandqueue;

import java.util.EmptyStackException;

public class MyQueue<T> {
    class Node<T> {
        private T data;
        private Node<T> next;

        public Node(T data) {
            this.data = data;
        }
    }

    StackV1<T> stackNewest, stackOldest;

    MyQueue() {
        stackNewest = new StackV1<>();
        stackOldest = new StackV1<>();
    }

    public int size() {
        return stackOldest.size() + stackNewest.size();
    }

    public void add(T item) {
        stackNewest.push(item);
    }

    private void shiftStacks() {
        if (stackOldest.isEmpty()) {
            while(!stackNewest.isEmpty()) {
                stackOldest.push(stackNewest.pop());
            }
        }
    }

    public T peek() {
        shiftStacks();
        return stackOldest.peek();
    }

    public T remove() {
        shiftStacks();
        return stackOldest.pop();
    }

    public boolean isEmpty() {
        return stackNewest.isEmpty() && stackOldest.isEmpty();
    }
}
