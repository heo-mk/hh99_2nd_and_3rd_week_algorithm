import math

# day_speed, night_loss, height = input().split()
# snail_day_speed, snail_night_loss, tree_height = int(day_speed), int(night_loss), int(height)

snail_day_speed, snail_night_loss, tree_height = map(int, input().split())
total_speed_per_day = snail_day_speed - snail_night_loss

day_it_takes = (tree_height - snail_night_loss) / total_speed_per_day
day_it_takes = math.ceil(day_it_takes)
print(day_it_takes)

# if (tree_height - snail_night_loss) % total_spped_per_day == 0:
#     day_it_takes = (tree_height - snail_night_loss)//total_spped_per_day
# else:
#     day_it_takes = (tree_height - snail_night_loss)//total_spped_per_day + 1
# print(day_it_takes)
