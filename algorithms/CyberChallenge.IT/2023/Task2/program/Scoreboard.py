from typing import List

"""
Who's the winner?

Problem: https://cyberchallenge.it/media/public/training/2023-winner.pdf
whiteboard: https://link.excalidraw.com/l/ATbTqvQ19d9/5gX3xyPnsoO
author: adambechtold
date: 2024.02.01
"""

class Task:
  def __init__(self, id: int, flag: str, points: int):
    self.id = id
    self.flag = flag
    self.points = points

  def __str__(self):
    return f"{self.id} {self.flag} {self.points}"

class Submission:
  def __init__(self, player_id: int, task_id: int, flag: str, time: int):
    self.player_id = player_id
    self.task_id = task_id
    self.flag = flag
    self.time = time

  def __str__(self):
    return ' '.join([str(x) for x in [self.player_id, self.task_id, self.flag, self.time]])

class Scoreboard:
  def __init__(self, number_of_players: int, number_of_tasks: int):
    self.scores = dict([(i + 1, Score(i + 1, 0, number_of_tasks)) for i in range(number_of_players)])
    # Key: Player Id
    # Value: Player's Score

  def raise_if_player_does_not_exist(self, player_id: int):
    if player_id not in self.scores:
      raise ValueError(f'Player {player_id} is not included in this scoreboard')

  def get_player_score(self, player_id: int) -> 'Score':
    self.raise_if_player_does_not_exist(player_id)
    return self.scores[player_id]


  def mark_task_completed(self, player_id: int, task: 'Task', time: int):
    self.raise_if_player_does_not_exist(player_id)
    player_score = self.scores[player_id]

    if task.id not in player_score.tasks_completions:
      # add points to sore
      player_score.value += task.points

      # Add task completion with this time
      player_score.tasks_completions[task.id] = TaskCompletion(task.id, time)

      # if task completed after earliest time, update earliest
      if player_score.earliest_time_score_achieved < time:
        player_score.earliest_time_score_achieved = time
    else:
      if time > player_score.earliest_time_score_achieved:
        # we already solved this question and this completion comes after our earliest seen completion
        # so we know we've already reflected that earlier solve
        pass
      else:
        # update earliest completion time for this task
        player_score.tasks_completions[task.id].earliest_completion_time = time

        # find last completed task
        latest_completed_time = 0
        for t in player_score.tasks_completions.values():
          latest_completed_time = max(latest_completed_time, t.earliest_completion_time)

        player_score.earliest_time_score_achieved = latest_completed_time

  def __str__(self):
    sorted_scores = sorted([s for s in self.scores.values()], reverse=True)
    return '\n'.join(str(score) for score in sorted_scores)


class TaskCompletion:
  def __init__(self, task_id: int, earliest_completion_time: int = 0):
    self.task_id = task_id
    self.earliest_completion_time  = earliest_completion_time


class Score:
  def __init__(self, player_id: int, value: int, num_tasks: int, earliest_time_score_achieved: int = 0):
    self.player_id = player_id
    self.value = value
    self.earliest_time_score_achieved = earliest_time_score_achieved
    self.tasks_completions = dict([])

  def __str__(self):
    return f"{self.player_id} {self.value}" # {self.earliest_time_score_achieved}"

  def __compare_scores__(self, other) -> int:
    if self.value > other.value:
      return 1
    elif self.value == other.value:
      return 0
    else:
      return -1

  def __compare_times__(self, other) -> int:
    if self.earliest_time_score_achieved > other.earliest_time_score_achieved:
      return -1
    elif self.earliest_time_score_achieved == other.earliest_time_score_achieved:
      return 0
    else:
      return 1

  def __compare_ids__(self, other) -> int:
    if self.player_id > other.player_id:
      return -1
    elif self.player_id == other.player_id:
      return 0
    else:
      return 1

  def __eq__(self, other):
    if isinstance(other, Score):
      comparisons = [self.__compare_scores__(other), self.__compare_times__(other), self.__compare_ids__(other)]
      return all(comparison == 0 for comparison in comparisons)
    return False

  def __lt__(self, other) -> bool:
    if isinstance(other, Score):
      if self.__eq__(other):
        return False

      comparisons = [self.__compare_scores__(other), self.__compare_times__(other), self.__compare_ids__(other)]
      for comparison in comparisons:
        if comparison == -1:
          return True
        if comparison == 1:
          return False
    return False

  def __le__(self, other) -> bool:
    if isinstance(other, Score):
      return self.__eq__(other) or self.__lt__(other)
    return False

  def __gt__(self, other) -> bool:
    if isinstance(other, Score):
      if self.__eq__(other):
        return False

      comparisons = [self.__compare_scores__(other), self.__compare_times__(other), self.__compare_ids__(other)]
      for comparison in comparisons:
        if comparison == 1:
          return True
        if comparison == -1:
          return False
    return False

  def __ge__(self, other):
    if isinstance(other, Score):
      return self.__eq__(other) or self.__gt__(other)
    return False


class Solution:
  def get_scoreboard(self, m: int, n: int, s: int, tasks: List['Task'], submissions: List['Submission']) -> Scoreboard:
    # m = number of players
    # n = number of tasks
    # s = number of submissions

    # 1 Create a lookup table of tasks
    task_lookup = dict([(task.id, task) for task in tasks])
    # 2 Create a scoreboard with each players score, earliest time score achieved, and tasks completed
    scoreboard = Scoreboard(m, n)

    for sub in submissions:
      if sub.flag == task_lookup[sub.task_id].flag:
        # This answer is correct
        scoreboard.mark_task_completed(sub.player_id, task_lookup[sub.task_id], sub.time)

    return scoreboard



example_input = """5 2 6
1 EfnccJSqUyOsYGO 50
2 XWMsVGHynvrEspF 100
2 2 XWMsVGHynvrEspF 7
2 1 EfnccJSqUyOsYGO 4
4 1 EfnccJSqUyOsYGO 10
1 1 EfnccJSqUyOsYGO 5
1 2 bWWinauoIIDfKpz 6
1 1 EfnccJSqUyOsYGO 25"""

#solution = Solution()
#solution.print_scoreboard(example_input)


"""
Pseudocode

1) create lookup table of tasks by task id # Runtime: O(t) # Memory: O(t)

2) create scoreboard # Runtime: O(p) # Memory O(p * t)
    for each player in range(1, m + 1) // for every player based on the number of players (1-indexed)
        score : int
        last valid submitted task : datetime
        tasks_completed : Map<id, earliest_completion_time>

3) for each submission # Runtime: O(s)
    if they got the answer correct
        if they have not completed this task before:
            add task.points to their score
            update scoreboard[player.id].last_valid_submission_time = submission.timestamp
       else
            if the timestamp of this submission is lower than the previous earliest_completion_time
                update task.earliest_completion_time

4) for each submission # O(s)
    finished_at: = max(task completed time of all tasks) # O(t)

5) sort submissions by points, timestamp, and player.id # O(s log(s))
"""
