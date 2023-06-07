from ...typings import Context


def setCleanUpTasksMiddleware(context: Context) -> Context:
    currentTask = context['tasksOrchestrator'].getCurrentTask(context)
    if currentTask is not None:
        # print(' ')
        # print(' ')
        # print('lastPressedKey', context['lastPressedKey'])
        # print('waypointIndex', context['cavebot']['waypoints']['currentIndex'])
        # print('currentTask', currentTask.name)
        # print('currentTask.status', currentTask.status)
        # if hasattr(currentTask, 'tasks'):
        #     print('currentTask.tasks', currentTask.tasks)
        #     print('currentTask.currentTaskIndex', currentTask.currentTaskIndex)
        if currentTask.isRootTask and currentTask.status == 'completed':
            context['tasksOrchestrator'].reset()
        if currentTask.rootTask is not None:
            # print('currentTask.rootTask', currentTask.rootTask.name)
            # print('currentTask.rootTask.status', currentTask.rootTask.status)
            # if hasattr(currentTask.rootTask, 'tasks'):
            #     print('currentTask.rootTask.tasks', currentTask.rootTask.tasks)
            #     print('len(currentTask.rootTask.tasks)', len(currentTask.rootTask.tasks))
            #     print('currentTask.rootTask.currentTaskIndex', currentTask.rootTask.currentTaskIndex)
            #     if hasattr(currentTask.rootTask.tasks[0], 'tasks'):
            #         print('childrenTasks', currentTask.rootTask.tasks[0].tasks)
            #         print('len(currentTask.rootTask.children.tasks)', len(currentTask.rootTask.tasks[0].tasks))
            #         print('currentTask.rootTask.children.currentTaskIndex', currentTask.rootTask.tasks[0].currentTaskIndex)
            if currentTask.rootTask.status == 'completed':
                context['tasksOrchestrator'].reset()
    return context
