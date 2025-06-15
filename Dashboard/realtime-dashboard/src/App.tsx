import Dashboard from './pages/Dashboard';
import { BrowserRouter, Routes, Route } from "react-router-dom"
import { Layout } from "@/components/layout/Layout"
// import TopDomainsPage from "@/pages/TopDomainsPage"


export default function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          
          <Route path="/" element={<Dashboard />} />
          {/* <Route path="/" element={<TopDomainsPage />} /> */}
          {/* Later you'll add: SummaryPage, TimelinePage, etc */}
        </Routes>
      </Layout>
    </BrowserRouter>
  )
}