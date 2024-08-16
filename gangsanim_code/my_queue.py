# q = [0] * 3
#
# front = -1
# rear = -1
#
# enqueue(1)
# front += 1
# q[front] = 1
#
# Q_size = 4
# cQ = [0]*Q_size
# front = rear = 0
#
# rear = (rear + 1) % Q_size
# cQ[rear] = 1
# rear = (rear + 1) % Q_size
# cQ[rear] = 2
# rear = (rear + 1) % Q_size
# cQ[rear] = 3
#
# front = (front+1)%Q_size
# cQ[rear]