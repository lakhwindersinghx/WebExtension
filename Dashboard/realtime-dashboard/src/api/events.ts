import  type { EventData } from "../types/EventData";

export async function fetchEvents(): Promise<EventData[]> {
  const response = await fetch('http://localhost:8000/events');
  if (!response.ok) throw new Error('Failed to fetch events');
  return await response.json();
}
