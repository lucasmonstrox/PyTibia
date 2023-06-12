from src.gameplay.core.tasks.common.base import BaseTask


context = {}

def test_should_delayBeforeStart_equal_0_when_delayBeforeStart_is_not_set():
    baseTask = BaseTask()
    assert baseTask.delayBeforeStart == 0

def test_should_delayBeforeStart_equal_1_when_delayBeforeStart_is_set_to_1():
    baseTask = BaseTask(delayBeforeStart=1)
    assert baseTask.delayBeforeStart == 1

def test_should_delayAfterComplete_equal_0_when_delayAfterComplete_is_not_set():
    baseTask = BaseTask()
    assert baseTask.delayAfterComplete == 0

def test_should_delayAfterComplete_equal_1_when_delayAfterComplete_is_set_to_1():
    baseTask = BaseTask(delayAfterComplete=1)
    assert baseTask.delayAfterComplete == 1

def test_should_delayOfTimeout_equal_0_when_delayOfTimeout_is_not_set():
    baseTask = BaseTask()
    assert baseTask.delayOfTimeout == 0

def test_should_delayOfTimeout_equal_1_when_delayOfTimeout_is_set_to_1():
    baseTask = BaseTask(delayOfTimeout=1)
    assert baseTask.delayOfTimeout == 1

def test_should_manuallyTerminable_equal_False_when_manuallyTerminable_is_not_set():
    baseTask = BaseTask()
    assert baseTask.manuallyTerminable == False

def test_should_manuallyTerminable_equal_True_when_manuallyTerminable_is_set_to_True():
    baseTask = BaseTask(manuallyTerminable=True)
    assert baseTask.manuallyTerminable == True

def test_should_isRootTask_equal_False_when_isRootTask_is_not_set():
    baseTask = BaseTask()
    assert baseTask.isRootTask == False

def test_should_isRootTask_equal_True_when_isRootTask_is_set_to_True():
    baseTask = BaseTask(isRootTask=True)
    assert baseTask.isRootTask == True

def test_should_name_equal_baseTask_when_name_is_not_set():
    baseTask = BaseTask()
    assert baseTask.name == 'baseTask'

def test_should_name_equal_customTask_when_name_is_set_to_customTask():
    baseTask = BaseTask(name='customTask')
    assert baseTask.name == 'customTask'

def test_should_parentTask_equal_None_when_parentTask_is_not_set():
    baseTask = BaseTask()
    assert baseTask.parentTask is None

def test_should_parentTask_equal_BaseTask_when_parentTask_is_set_to_BaseTask():
    parentTask = BaseTask()
    baseTask = BaseTask(parentTask=parentTask)
    assert baseTask.parentTask == parentTask

def test_should_ignore():
    baseTask = BaseTask()
    assert baseTask.shouldIgnore(context) == False

def test_shouldManuallyComplete():
    baseTask = BaseTask()
    assert baseTask.shouldManuallyComplete(context) == False

def test_shouldRestart():
    baseTask = BaseTask()
    assert baseTask.shouldRestart(context) == False

def test_do():
    baseTask = BaseTask()
    assert baseTask.do(context) == context

def test_did():
    baseTask = BaseTask()
    assert baseTask.did(context) == True

def test_ping():
    baseTask = BaseTask()
    assert baseTask.ping(context) == context

def test_onBeforeStart():
    baseTask = BaseTask()
    assert baseTask.onBeforeStart(context) == context

def test_onIgnored():
    baseTask = BaseTask()
    assert baseTask.onIgnored(context) == context

def test_onInterrupt():
    baseTask = BaseTask()
    assert baseTask.onInterrupt(context) == context

def test_onComplete():
    baseTask = BaseTask()
    assert baseTask.onComplete(context) == context

def test_onTimeout():
    baseTask = BaseTask()
    assert baseTask.onTimeout(context) == context