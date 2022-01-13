from homework6.task1 import User


def test_class_counter():
    """Testing that counter counts number of instances.
    And reset instances returns number of creations before deletion."""
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == user.reset_instances_counter()


def test_class_counter_instance():
    """Testing that counter counts number of instances correctly
    when accessing via class instance """
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3
    user.reset_instances_counter()


def test_class_counter_class():
    """Testing that counter counts number of instances correctly
    when accessing via class
    """
    _, _ = User(), User()
    assert User.get_created_instances() == 2


def test_class_reset_counter_class():
    """Testing that reset using class counter deletes
    number of created class elements
    """
    user, _, _ = User(), User(), User()
    User.reset_instances_counter()
    assert user.get_created_instances() == 0


def test_class_reset_counter_instance():
    """Testing that reset using instance counter deletes
     number of created class elements
     """
    user, _, _ = User(), User(), User()
    user.reset_instances_counter()
    assert user.get_created_instances() == 0


def test_class_reset_counter_when_empty():
    """Testing that reset returns correct value
    when calling it before creating any instances
     """
    assert User.reset_instances_counter() == 0
