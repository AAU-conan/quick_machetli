begin_version
3
end_version
begin_metric
1
end_metric
4
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
36
Atom fuel(t0, level0)
Atom fuel(t0, level1)
Atom fuel(t0, level10)
Atom fuel(t0, level11)
Atom fuel(t0, level12)
Atom fuel(t0, level13)
Atom fuel(t0, level14)
Atom fuel(t0, level15)
Atom fuel(t0, level16)
Atom fuel(t0, level17)
Atom fuel(t0, level18)
Atom fuel(t0, level19)
Atom fuel(t0, level2)
Atom fuel(t0, level20)
Atom fuel(t0, level21)
Atom fuel(t0, level22)
Atom fuel(t0, level23)
Atom fuel(t0, level24)
Atom fuel(t0, level25)
Atom fuel(t0, level26)
Atom fuel(t0, level27)
Atom fuel(t0, level28)
Atom fuel(t0, level29)
Atom fuel(t0, level3)
Atom fuel(t0, level30)
Atom fuel(t0, level31)
Atom fuel(t0, level32)
Atom fuel(t0, level33)
Atom fuel(t0, level34)
Atom fuel(t0, level36)
Atom fuel(t0, level4)
Atom fuel(t0, level5)
Atom fuel(t0, level6)
Atom fuel(t0, level7)
Atom fuel(t0, level8)
Atom fuel(t0, level9)
end_variable
begin_variable
var2
-1
5
Atom at(p2, l0)
Atom at(p2, l1)
Atom at(p2, l2)
Atom at(p2, l3)
Atom in(p2, t0)
end_variable
begin_variable
var3
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
29
3
1
end_state
begin_goal
1
3 0
end_goal
7
begin_operator
drive t0 l1 l3 level22 level11 level33
0
2
0 0 1 3
0 1 27 15
1
end_operator
begin_operator
drive t0 l2 l1 level33 level3 level36
0
2
0 0 2 1
0 1 29 27
1
end_operator
begin_operator
drive t0 l3 l2 level16 level6 level22
0
2
0 0 3 2
0 1 15 8
1
end_operator
begin_operator
load p1 t0 l1
1
0 1
1
0 3 1 4
1
end_operator
begin_operator
load p2 t0 l3
1
0 3
1
0 2 3 4
1
end_operator
begin_operator
unload p1 t0 l0
1
0 0
1
0 3 4 0
1
end_operator
begin_operator
unload p1 t0 l1
1
0 1
0
1
end_operator
0
