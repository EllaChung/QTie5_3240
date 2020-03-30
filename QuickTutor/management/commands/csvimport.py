from QuickTutor.models import Class
from django.core.management.base import BaseCommand

# path_to_csv = '../../../staticfiles/data/UVA_Courses_S20.csv'
class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    insert_count=Class.objects.from_csv(
      '../../UVA_Courses_S20.csv',
      dict(class_name='CLASS_NAME', dept='DEPT', course_num='COURSE_NUM', course_topic='COURSE_TOPIC')
      )
    print("{} Classes inserted".format(insert_count))