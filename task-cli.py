import argparse
from TaskManager import TaskManager

def main():
    manager = TaskManager('tasks.json')

    parser = argparse.ArgumentParser(prog='task-cli',description='Task Tracker CLI app')
    subparser = parser.add_subparsers(dest='command')

    #Add command
    add_parser = subparser.add_parser('add',help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

    #Update command
    update_parser = subparser.add_parser('update',help='Update a task')
    update_parser.add_argument('id', type=int, help="Task id")
    update_parser.add_argument('description', type=str, help="New description")

    #Delete command
    delete_parser = subparser.add_parser('delete',help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task id')

    #Mark in progress command
    in_progress = subparser.add_parser('mark-in-progress', help='Mark a task in progress')
    in_progress.add_argument('id',type=int,help='Task id')

    #Mark done command
    done = subparser.add_parser('mark-done', help='Mark a task done')
    done.add_argument('id',type=int,help='Task id')

    #List command
    list = subparser.add_parser('list',help='List tasks')
    list.add_argument(
        'status',
        nargs='?',
        choices=['done','todo','in-progress'],
        help="List tasks filter by status")

    #Handle command
    args = parser.parse_args()
    
    if args.command == 'add':
        description = args.description
        manager.addTask(description)

    elif args.command == 'update':
        id = args.id
        description = args.description
        manager.updateTask(id,description)

    elif args.command == 'delete':
        id = args.id
        manager.updateTaskStatus(id,'deleted')

    elif args.command == 'mark-in-progress':
        id = args.id
        manager.updateTaskStatus(id,'in-progress')

    elif args.command == 'mark-done':
        id = args.id
        manager.updateTaskStatus(id,'done')
    
    elif args.command == 'list':
        status = args.status
        if status:
            manager.listTasks(status)
        else:
            manager.listTasks()

    else:
        parser.print_help()



if __name__ == "__main__":
    main()