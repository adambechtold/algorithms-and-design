import sys
from Scoreboard import Solution, Submission, Task

solution = Solution()

def main():
  # m = number of players
  # n = number of tasks (flags)
  # s = number of submissions
  rows = []

  for line in sys.stdin:
    rows.append(line.strip())

  config = rows[0].split(' ')
  num_players = int(config[0])
  num_tasks = int(config[1])
  num_submissions = int(config[2])

  task_list = []
  for row in rows[1: num_tasks + 1]:
    task_config = row.split(' ')
    id = int(task_config[0])
    flag = task_config[1]
    points = int(task_config[2])
    task_list.append(Task(id, flag, points))

  submission_list = []
  for row in rows[num_tasks + 1: len(rows)]:
    submission_config = row.split(' ')
    player_id = int(submission_config[0])
    task_id = int(submission_config[1])
    flag = submission_config[2]
    time = int(submission_config[3])

    submission_list.append(Submission(player_id, task_id, flag, time))

  scoreboard = solution.get_scoreboard(num_players, num_tasks, num_submissions, task_list, submission_list)
  print(scoreboard)

if __name__ == "__main__":
  main()
