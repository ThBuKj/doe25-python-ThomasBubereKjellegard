class Alarm:
    def __init__(self, metric_type, threshold):
        self.metric_type = metric_type
        self.threshold = threshold

    def __str__(self):
        return f"{self.metric_type} larm {self.threshold}%"

