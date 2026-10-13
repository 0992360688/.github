"use client";

import { ModeProvider, useMode } from "@/context/ModeContext";
import ModeSwitch from "@/app/components/mentor-mode/ModeSwitch";

function Screen() {
  const { mode } = useMode();
  // Placeholders until Task 14 merges; then this becomes <MyDoubts /> / <MentorDashboard />.
  return (
    <p className="font-display text-xl text-ink">
      {mode === "learner" ? "Learner view goes here" : "Mentor view goes here"}
    </p>
  );
}

export default function MentorModePage() {
  return (
    <ModeProvider>
      <main className="min-h-screen bg-cream px-4 py-10">
        <div className="mx-auto flex max-w-2xl flex-col gap-6">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <h1 className="font-display text-3xl font-bold text-ink">Mentor Mode</h1>
            <ModeSwitch />
          </div>
          <Screen />
        </div>
      </main>
    </ModeProvider>
  );
}
