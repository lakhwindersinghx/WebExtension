export interface EventData {
  id: string;
  tab_url: string;
  title: string;
  scroll_depth: number; // 0–100
  duration_seconds: number | null;
  category: string;
  timestamp: string;
}
