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
2
Atom not_blocked(seg_ppdoor_0_40, airplane_daewh)
NegatedAtom not_blocked(seg_ppdoor_0_40, airplane_daewh)
end_variable
begin_variable
var1
-1
4
Atom is-moving(airplane_daewh)
Atom is-parked(airplane_daewh, seg_pp_0_60)
Atom is-pushing(airplane_daewh)
<none of those>
end_variable
begin_variable
var2
-1
15
Atom airborne(airplane_daewh, seg_rwe_0_50)
Atom airborne(airplane_daewh, seg_rww_0_50)
Atom at-segment(airplane_daewh, seg_pp_0_60)
Atom at-segment(airplane_daewh, seg_ppdoor_0_40)
Atom at-segment(airplane_daewh, seg_rw_0_400)
Atom at-segment(airplane_daewh, seg_rwe_0_50)
Atom at-segment(airplane_daewh, seg_rww_0_50)
Atom at-segment(airplane_daewh, seg_twe1_0_200)
Atom at-segment(airplane_daewh, seg_twe2_0_50)
Atom at-segment(airplane_daewh, seg_twe3_0_50)
Atom at-segment(airplane_daewh, seg_twe4_0_50)
Atom at-segment(airplane_daewh, seg_tww1_0_200)
Atom at-segment(airplane_daewh, seg_tww2_0_50)
Atom at-segment(airplane_daewh, seg_tww3_0_50)
Atom at-segment(airplane_daewh, seg_tww4_0_50)
end_variable
14
begin_mutex_group
4
1 0
1 2
2 0
2 1
end_mutex_group
begin_mutex_group
1
2 2
end_mutex_group
begin_mutex_group
1
2 3
end_mutex_group
begin_mutex_group
1
2 4
end_mutex_group
begin_mutex_group
1
2 5
end_mutex_group
begin_mutex_group
1
2 6
end_mutex_group
begin_mutex_group
1
2 7
end_mutex_group
begin_mutex_group
1
2 8
end_mutex_group
begin_mutex_group
1
2 9
end_mutex_group
begin_mutex_group
1
2 10
end_mutex_group
begin_mutex_group
1
2 11
end_mutex_group
begin_mutex_group
1
2 12
end_mutex_group
begin_mutex_group
1
2 13
end_mutex_group
begin_mutex_group
1
2 14
end_mutex_group
begin_state
0
2
2
end_state
begin_goal
1
2 0
end_goal
4
begin_operator
park_seg_pp_0_60_south airplane_daewh
1
2 2
2
0 0 -1 0
0 1 0 1
1
end_operator
begin_operator
pushback_seg_pp_0_60_seg_ppdoor_0_40_south_south_medium airplane_daewh) and then (pushback_seg_ppdoor_0_40_seg_tww1_0_200_south_north_medium airplane_daewh) and then (startup_seg_tww1_0_200_north_medium airplane_daewh) and then (move_seg_tww1_0_200_seg_twe1_0_200_north_south_medium airplane_daewh) and then (move_seg_twe1_0_200_seg_twe2_0_50_south_south_medium airplane_daewh) and then (move_seg_twe2_0_50_seg_twe3_0_50_south_south_medium airplane_daewh) and then (move_seg_twe3_0_50_seg_twe4_0_50_south_south_medium airplane_daewh) and then (move_seg_twe4_0_50_seg_rwe_0_50_south_south_medium airplane_daewh) and then (takeoff_seg_rwe_0_50_south airplane_daewh
0
3
0 0 0 1
0 1 2 0
0 2 2 0
9
end_operator
begin_operator
startup_seg_pp_0_60_north_medium airplane_daewh
1
2 2
1
0 1 2 0
1
end_operator
begin_operator
startup_seg_pp_0_60_south_medium airplane_daewh
1
2 2
2
0 0 0 1
0 1 2 0
1
end_operator
0
