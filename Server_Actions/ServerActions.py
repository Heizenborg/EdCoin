from Classes.Block import Block
import datetime
import threading
from Classes.Contract import Course, CourseContract


def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, datetime.datetime.now(), ["Genesis Block"], "0")

def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = datetime.datetime.now()
  this_data = ["Hey! I'm block " + str(this_index)]
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)

def make_courses(myCourses):
  courses = []
  for course in myCourses:
    courses.append(Course(title=course, status=False, school="My School"))

  return courses

def make_new_contract(transmission):
  print("MAKE NEW CONTRACT")
  new_transmission = transmission.split(':')
  transmitted_courses = new_transmission[2]
  courses = transmitted_courses.split(',')

  courses_array = make_courses(courses)

  Contract = CourseContract(student=new_transmission[0], complete=False, courses=courses_array)

  print("new contract for " + str(new_transmission[0])) 
  return Contract