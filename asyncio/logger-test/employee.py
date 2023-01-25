import my_logger
import asyncio_logging

asyncio_logging.setup_logging_queue()

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        my_logger.logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John1', 'Smith')
emp_2 = Employee('Corey1', 'Schafer')
emp_3 = Employee('Jane1', 'Doe')
