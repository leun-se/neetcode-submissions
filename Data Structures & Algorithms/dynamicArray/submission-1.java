class DynamicArray {
    private int[] array;
    private int size; // number of elements in array

    public DynamicArray(int capacity) {
        if (capacity <= 0) {
            throw new IllegalArgumentException("Capacity must be > 0");
        }
        array = new int[capacity];
        size = 0;
    }

    public int get(int i) {
        if (i < 0 || i >= size) {
            throw new IndexOutOfBoundsException();
        }
        return array[i];
    }

    public void set(int i, int n) {
        if (i < 0 || i >= size) {
            throw new IndexOutOfBoundsException();
        }
        array[i] = n;
    }

    public void pushback(int n) {
        if (size == array.length) {
            resize();
        }
        array[size] = n;
        size++;
    }

    public int popback() {
        if (size == 0) {
            throw new IllegalStateException("Array is empty");
        }
        int temp = array[size - 1];
        size--;
        return temp;
    }

    private void resize() {
        int[] temp = new int[array.length * 2];
        for (int i = 0; i < array.length; i++) {
            temp[i] = array[i];
        }
        array = temp;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return array.length;
    }
}
