
import datetime
import gantt

# Change font default
gantt.define_font_attributes(fill='black',
                             stroke='black',
                             stroke_width=0,
                             font_family="Verdana")

DE = gantt.Resource('DE')

# Create some tasks
t1 = gantt.Task(name='Complete project plan',
                start=datetime.date(2018, 10, 15),
                duration=1,
                resources=[DE],
                percent_done=100,
                color="#FF8080")

t2 = gantt.Task(name='Write user requirements document',
                start=datetime.date(2018, 10, 16),
                duration=1,
                resources=[DE],
                color="#FF8080",
                percent_done=100,
                depends_of=t1)

t3 = gantt.Task(name='learn Docker syntax',
                start=datetime.date(2018, 10, 17),
                duration=7,
                resources=[DE],
                percent_done=100,
                color="#FF8080",
                depends_of=t2)

t4 = gantt.Task(name='Create FASTQC container',
                start=datetime.date(2018, 10, 24),
                duration=3,
                resources=[DE],
                percent_done=100,
                color="#FF8080",
                depends_of=t3)

t5 = gantt.Task(name='Test FASTQC container',
                start=datetime.date(2018, 10, 29),
                duration=1,
                resources=[DE],
                percent_done=100,
                color="#FF8080",
                depends_of=t4)

t6 = gantt.Task(name='Create Trimmomatic container',
                start=datetime.date(2018, 10, 30),
                duration=3,
                resources=[DE],
                percent_done=100,
                color="#FF8080",
                depends_of=t5)

t7 = gantt.Task(name='Test Trimmomatic container',
                start=datetime.date(2018, 11, 2),
                duration=1,
                resources=[DE],
                percent_done=100,
                color="#FF8080",
                depends_of=t6)

t8 = gantt.Task(name='Create BWA-MEM container',
                start=datetime.date(2018, 11, 5),
                duration=3,
                resources=[DE],
                percent_done=100,
                color="#FF8080",
                depends_of=t7)

t9 = gantt.Task(name='Test BWA-MEM container',
                start=datetime.date(2018, 11, 8),
                duration=1,
                resources=[DE],
                percent_done=100,
                color="#FF8080",
                depends_of=t8)

t10 = gantt.Task(name='Learn CWL specification syntax',
                start=datetime.date(2018, 11, 9),
                duration=7,
                resources=[DE],
                percent_done=100,
                color="#FF8080",
                depends_of=t9)

t11 = gantt.Task(name='Write CWL specification',
                start=datetime.date(2018, 11, 16),
                duration=5,
                resources=[DE],
                percent_done=100,
                color="#FF8080",
                depends_of=t10)

t12 = gantt.Task(name='Test CWL specification',
                start=datetime.date(2018, 11, 21),
                duration=1,
                resources=[DE],
                percent_done=100,
                color="#FF8080",
                depends_of=t11)

t13 = gantt.Task(name='Develop test plan for file mount',
                start=datetime.date(2018, 11, 22),
                duration=7,
                resources=[DE],
                percent_done=100,
                color="#FF8080",
                depends_of=t12)

t14 = gantt.Task(name='Complete file mount test',
                start=datetime.date(2018, 11, 29),
                duration=1,
                resources=[DE],
                percent_done=100,
                color="#FF8080",
                depends_of=t13)

t15 = gantt.Task(name='Complete User Acceptance Test',
                start=datetime.date(2018, 11, 30),
                duration=4,
                resources=[DE],
                percent_done=100,
                color="#FF8080",
                depends_of=t14)

t16 = gantt.Task(name='Create SOP for project',
                start=datetime.date(2018, 12, 4),
                duration=1,
                resources=[DE],
                percent_done=100,
                color="#FF8080",
                depends_of=t15)


#Create a project


p1 = gantt.Project(name='IT for Advanced Bioinformatics Applications')


# Add tasks

p1.add_task(t1)
p1.add_task(t2)
p1.add_task(t3)
p1.add_task(t4)
p1.add_task(t5)
p1.add_task(t6)
p1.add_task(t7)
p1.add_task(t8)
p1.add_task(t9)
p1.add_task(t10)
p1.add_task(t11)
p1.add_task(t12)
p1.add_task(t13)
p1.add_task(t14)
p1.add_task(t15)
p1.add_task(t16)


# Draw diagram
p1.make_svg_for_tasks(filename='advance_it_gantt_chart.svg',
                      today=datetime.date(2018, 10, 15),
                      start=datetime.date(2018,10, 10),
                      end=datetime.date(2018, 12, 22))
