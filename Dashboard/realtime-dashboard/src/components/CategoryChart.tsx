import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import type { EventData } from '../types/EventData';

interface Props {
  data: EventData[];
}

export const CategoryChart = ({ data }: Props) => {
  if (!data || data.length === 0) {
  return <p className="text-gray-500">No data available to render chart.</p>;
}
  const aggregated = data.reduce<Record<string, number>>((acc, event) => {
    const duration = event.duration_seconds ?? 0;
    
    acc[event.category] = (acc[event.category] || 0) + duration;
    return acc;
  }, {});

  const chartData = Object.entries(aggregated).map(([category, total]) => ({
    category,
    total,
  }));
  console.log('Chart data:', chartData);

  return (
    <div className="w-full h-64 bg-white rounded-xl shadow p-4 mb-6">
      <h2 className="text-xl font-semibold mb-4">Time Spent by Category</h2>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={chartData}>
          <XAxis dataKey="category" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="total" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};
