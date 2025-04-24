begin_version
3
end_version
begin_metric
1
end_metric
3
begin_variable
var0
-1
4
Atom at(t0, l0)
Atom at(t0, l1)
Atom at(t0, l2)
Atom at(t0, l3)
end_variable
begin_variable
var1
-1
5
Atom at(p2, l0)
Atom at(p2, l1)
Atom at(p2, l2)
Atom at(p2, l3)
Atom in(p2, t0)
end_variable
begin_variable
var2
-1
5
Atom at(p1, l0)
Atom at(p1, l1)
Atom at(p1, l2)
Atom at(p1, l3)
Atom in(p1, t0)
end_variable
0
begin_state
2
3
1
end_state
begin_goal
2
1 0
2 0
end_goal
5
begin_operator
drive t0 l1 l3 level22 level11 level33
0
1
0 0 1 3
1
end_operator
begin_operator
drive t0 l2 l1 level33 level3 level36
0
1
0 0 2 1
1
end_operator
begin_operator
drive t0 l2 l3 level10 level6 level16
0
1
0 0 2 3
1
end_operator
begin_operator
drive t0 l3 l0 level4 level18 level22) and then (unload p1 t0 l0) and then (drive t0 l0 l2 level2 level2 level4
0
2
0 0 3 2
0 2 4 0
3
end_operator
begin_operator
load p1 t0 l1
1
0 1
1
0 2 1 4
1
end_operator
0
