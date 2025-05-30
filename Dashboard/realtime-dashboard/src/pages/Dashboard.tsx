import { useEffect, useState } from 'react';
import { fetchEvents } from '../api/events';
import type { EventData } from '../types/EventData';
import { CategoryChart } from '../components/ui/bargraph';

import { SessionTable } from '../components/SessionTable';

export default function Dashboard() {
  const [events, setEvents] = useState<EventData[]>([]);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchEvents()
      .then(setEvents)
      .catch((err) => setError(err.message));
  }, []);

  return (
    <main className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-3xl font-bold mb-6">Activity Dashboard</h1>
        {error && <p className="text-red-600">{error}</p>}
        <CategoryChart data={events} />

        <SessionTable data={events.slice(0, 20)} />
      </div>
    </main>
  );
}
