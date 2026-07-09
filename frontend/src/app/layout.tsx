import type { Metadata } from "next";
import "./globals.css";

// This is the ROOT layout. Every page in the app is wrapped by this.
// We are not designing it yet - this is just the minimum needed
// for the app to run.

export const metadata: Metadata = {
  title: "AI Tools Directory",
  description: "Discover the best AI tools in one place.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
