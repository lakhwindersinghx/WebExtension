"use client"

import { TrendingUp } from "lucide-react"
import { Bar, BarChart, CartesianGrid, LabelList, XAxis, YAxis } from "recharts"
import type { EventData } from "@/types/EventData"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { type ChartConfig, ChartContainer, ChartTooltip, ChartTooltipContent } from "@/components/ui/chart"
// import { ChartLegend, ChartLegendContent } from "@/components/ui/chart"

interface Props {
  data: EventData[]
}

export const CategoryChart = ({ data }: Props)  => {
  if (!data || data.length === 0) {
    return (
      <Card className="p-4">
        <p className="text-gray-500">No data available to render chart.</p>
      </Card>
    )
  }

  // Aggregate duration by category
  const aggregated = data.reduce<Record<string, number>>((acc, event) => {
    const duration = event.duration_seconds ?? 0
    acc[event.category] = (acc[event.category] || 0) + duration
    return acc
  }, {})

  const chartData = Object.entries(aggregated)
    .map(([category, total]) => ({ category, total }))
    .sort((a, b) => b.total - a.total) // Sort descending by duration

  console.log("Chart data", chartData)

  const chartConfig = {
    total: {
      label: "Time Spent (s)",
      // color: "hsl(217, 91%, 60%)", // Nice blue color like in your reference image
    },
  } satisfies ChartConfig

  return (
    <Card>
      <CardHeader>
        <CardTitle>Time Spent by Category</CardTitle>
        <CardDescription>Based on recent tracked sessions</CardDescription>
      </CardHeader>
      <CardContent>
        <ChartContainer config={chartConfig} className="h-64 w-full">
          <BarChart
            data={chartData}
            margin={{
              top: 20,
              right: 20,
              bottom: 20,
              left: 20,
            }}
            barCategoryGap="20%"
          >
            <CartesianGrid vertical={false} strokeDasharray="3 3" stroke="#e0e0e0" />
            <XAxis
              dataKey="category"
              tickLine={false}
              tickMargin={10}
              axisLine={false}
              tick={{ fontSize: 12, fill: "#666" }}
            />
            <YAxis
              allowDecimals={false}
              domain={[0, "dataMax"]}
              tick={{ fontSize: 12, fill: "#666" }}
              axisLine={false}
              tickLine={false}
            />
            <ChartTooltip content={<ChartTooltipContent hideLabel />} />
            {/* <ChartLegend content={<ChartLegendContent />} / */}
            <Bar dataKey="total" fill="hsl(217, 91%, 60%)" radius={[8, 8, 0, 0]} maxBarSize={60}>
              <LabelList
                dataKey="total"
                position="top"
                offset={8}
                className="fill-foreground"
                fontSize={12}
                fontWeight={600}
              />
            </Bar>
          </BarChart>
        </ChartContainer>
      </CardContent>
      <CardFooter className="flex-col items-start gap-2 text-sm">
        {/* <div className="flex gap-2 font-medium leading-none">
          Trending up by 5.2% this month <TrendingUp className="h-4 w-4" />
        </div> */}
        <div className="leading-none text-muted-foreground">Showing total time by category</div>
      </CardFooter>
    </Card>
  )
}
