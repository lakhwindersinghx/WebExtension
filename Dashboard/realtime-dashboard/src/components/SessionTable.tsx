import type  { EventData } from '../types/EventData';

interface Props {
  data: EventData[];
}
function formatDuration(seconds: number | null) {
  if (!seconds || seconds < 1) return "0s";
  const min = Math.floor(seconds / 60);
  const sec = seconds % 60;
  return `${min > 0 ? `${min}m ` : ""}${sec}s`;
}

function truncate(text: string, max = 60) {
  return text.length > max ? text.slice(0, max) + "..." : text;
}


export const SessionTable = ({ data }: Props) => (
  <div className="bg-white rounded-xl shadow p-4">
    <h2 className="text-xl font-semibold mb-4">Recent Sessions</h2>
    <div className="overflow-auto">
      <table className="min-w-full text-sm">
        <thead className="border-b bg-gray-100">
          <tr>
            <th className="text-left px-3 py-2">Title</th>
            <th className="text-left px-3 py-2">Scroll %</th>
            <th className="text-left px-3 py-2">Duration (s)</th>
            <th className="text-left px-3 py-2">Category</th>
            <th className="text-left px-3 py-2">Time</th>
          </tr>
        </thead>
        <tbody>
          {data.map(event => (
            <tr key={event.id} className="border-b hover:bg-gray-50">
              <td className="px-3 py-2 max-w-xs truncate">{event.title}</td>
              <td className="px-3 py-2">{event.scroll_depth}%</td>
              <td className="px-3 py-2">
              <td>{formatDuration(event.duration_seconds)}</td>

                {/* {typeof event.duration_seconds === 'number' ? event.duration_seconds : 'N/A'} */}
              </td>
              <td className="px-3 py-2 capitalize">{event.category}</td>
              <td className="px-3 py-2 text-xs text-gray-500">
                {new Date(event.timestamp).toLocaleTimeString()}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  </div>
);
