import turtle as t

t.color("yellow")
t.begin_fill()
t.left(36)
for x in range(10):
	t.forward(30)
  if x % 2 == 0:
		t.right(108)
	else:
		t.left(36)
t.end_fill()
