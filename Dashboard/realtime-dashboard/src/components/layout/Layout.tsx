// src/components/Layout.tsx
import type { ReactNode } from "react"
import { NavigationMenu, NavigationMenuItem, NavigationMenuList, NavigationMenuLink } from "@/components/ui/navigation-menu"
import { Link } from "react-router-dom"  // if you're using react-router

interface LayoutProps {
  children: ReactNode
}

export function Layout({ children }: LayoutProps) {
  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-white shadow px-6 py-4"  >
        <NavigationMenu>
          <NavigationMenuList className="space-x-4">
            <NavigationMenuItem><NavLink to="/">Home</NavLink></NavigationMenuItem>
            {/* <NavigationMenuItem><NavLink to="/summary">Summary</NavLink></NavigationMenuItem>
            <NavigationMenuItem><NavLink to="/timeline">Timeline</NavLink></NavigationMenuItem>
            <NavigationMenuItem><NavLink to="/domains">Domains</NavLink></NavigationMenuItem>
            <NavigationMenuItem><NavLink to="/categories">Categories</NavLink></NavigationMenuItem> */}
          </NavigationMenuList>
        </NavigationMenu>
      </header>
      <main className="p-6">{children}</main>
    </div>
  )
}

function NavLink({ to, children }: { to: string; children: ReactNode }) {
  return (
    <NavigationMenuLink asChild>
      <Link className="font-medium text-gray-700 hover:text-blue-500" to={to}>
        {children}
      </Link>
    </NavigationMenuLink>
  )
}
