document.getElementById("addTaskButton").onclick = function() {
    const taskInput = document.getElementById("taskInput").value;
    if (taskInput) {
        fetch('/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ content: taskInput }),
        }).then(response => response.json())
          .then(task => {
              const li = document.createElement("li");
              li.textContent = task.content;
              
              const deleteButton = document.createElement("button");
              deleteButton.textContent = "Delete";
              deleteButton.onclick = function() {
                  fetch(`/tasks/${task.id}`, { method: 'DELETE' });
                  li.remove();
              };
              
              li.appendChild(deleteButton);
              document.getElementById("taskList").appendChild(li);
              document.getElementById("taskInput").value = '';
          });
    }
};
