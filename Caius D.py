'''
Calculating Caius D size from The Titan's bride
This is not the cleanest code and it was made for fun
'''

# Japan men's national basketball team. 2021 FIBA Asia Cup qualification roster
Basketball_players_height = [206, 181, 167, 191, 186, 207, 190, 192, 207, 192, 206, 198]
average_individual_height = sum(Basketball_players_height)/float(len(Basketball_players_height))

kouichi_height = average_individual_height
print('Kouichi real height: ' + str(kouichi_height))

#Scale factor from chapter 7 (both standing sraight, in centimeters) using
# isolation method
manga_lenght_Caius_chapter7 = 6
manga_lenght_Kouichi_chapter7 = 4.5
scale_factor_Kouichi_to_Caius_chapter7 = manga_lenght_Caius_chapter7 / manga_lenght_Kouichi_chapter7 #this is 4/3
scale_factor_Caius_to_Kouichi_chapter7 = manga_lenght_Kouichi_chapter7 / manga_lenght_Caius_chapter7

manga_lenght_Caius_chapter9 = 7
manga_lenght_Kouichi_chapter9 = 5
scale_factor_Kouichi_to_Caius_chapter9 = manga_lenght_Caius_chapter9 / manga_lenght_Kouichi_chapter9
scale_factor_Caius_to_Kouichi_chapter9 = manga_lenght_Kouichi_chapter9 / manga_lenght_Caius_chapter9

#calculating the averages for scale factor
scale_factor_Kouichi_to_Caius = (scale_factor_Kouichi_to_Caius_chapter9 + scale_factor_Kouichi_to_Caius_chapter7) / 2
scale_factor_Caius_to_Kouichi = (scale_factor_Caius_to_Kouichi_chapter9 + scale_factor_Caius_to_Kouichi_chapter7) / 2

#Using scale factor to calculate real height Caius in centimeters
real_height_Caius = kouichi_height * scale_factor_Kouichi_to_Caius
print('Caius real heigth: ' + str(real_height_Caius))

#Caius D seems to have a lenght from Kouichi hip to knee (References: Chapter 10 and 14)
# Using the scale factor to calculate the real average distance of Kouichi hip-knee
# considering that hip to knee seems to be 26.87% of his heigth based on panels from chapters 1, 7 and, 9
# assuming Kouichi real heigth is 193.58
lenght1_knee_hip = 8
lenght2_knee_hip = 10.5
lenght3_knee_hip = 7.5

real_hip_knee_distance = (26.87 * kouichi_height) / 100
scale_f_hip_knee1 = real_hip_knee_distance / lenght1_knee_hip
scale_f_hip_knee2 = real_hip_knee_distance / lenght2_knee_hip
scale_f_hip_knee3 = real_hip_knee_distance / lenght3_knee_hip

average_scale_f_hip_knee = (scale_f_hip_knee1 + scale_f_hip_knee2 + scale_f_hip_knee3) / 3
lenght1_knee_hip_to_real = lenght1_knee_hip * average_scale_f_hip_knee
lenght2_knee_hip_to_real = lenght2_knee_hip * average_scale_f_hip_knee
lenght3_knee_hip_to_real = lenght3_knee_hip * average_scale_f_hip_knee

# Size of Caius D using as reference Kouichi lenghts: lenght1_knee_hip_to_real 1, 2 and 3
size_Caius_D = (lenght1_knee_hip_to_real + lenght2_knee_hip_to_real + lenght3_knee_hip_to_real) / 3
print('Size of Caius D: ' + str(size_Caius_D))