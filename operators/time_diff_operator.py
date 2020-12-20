from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from datetime import date


class TimeDiff(BaseOperator):

    @apply_defaults
    def __init__(self, diff_date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.diff_date = diff_date

    def execute(self, context):
        print('Date diff: ', abs((date.today() - self.diff_date).days))
