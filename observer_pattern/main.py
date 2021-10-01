from observer_pattern.subject import CricketScore
from observer_pattern.observer import RunsDisplay, WicketsDisplay

if __name__ == '__main__':
    cricket_score_obj = CricketScore()
    runs_display_obj = RunsDisplay(cricket_score_obj)
    wickets_display_obj = WicketsDisplay(cricket_score_obj)

    cricket_score_obj.runs = 2
    cricket_score_obj.runs = 4
    cricket_score_obj.wickets = 1
    cricket_score_obj.runs = 6

    cricket_score_obj.remove_observer(wickets_display_obj)
    cricket_score_obj.runs = 10
