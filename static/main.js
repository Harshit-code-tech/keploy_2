function fetchEvents() {
  fetch('/api/events')
    .then(res => res.json())
    .then(events => {
      const list = document.getElementById('eventsList');
      if (events.length === 0) {
        list.innerHTML = '<div class="alert alert-info">No events found. Add one above!</div>';
      } else {
        list.innerHTML = events.map(e => `
          <div class="card mb-2">
            <div class="card-body">
              <h5>${e.title}</h5>
              <p>${e.description || ''}</p>
              <button onclick="deleteEvent(${e.id})" class="btn btn-danger btn-sm">Delete</button>
            </div>
          </div>
        `).join('');
      }
    });
}

function deleteEvent(id) {
  fetch(`/api/events/${id}`, { method: 'DELETE' })
    .then(() => fetchEvents());
}

document.getElementById('eventForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const title = document.getElementById('title').value;
  const description = document.getElementById('description').value;

  fetch('/api/events', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, description })
  })
  .then(() => {
    document.getElementById('eventForm').reset();
    fetchEvents();
  });
});

fetchEvents();
