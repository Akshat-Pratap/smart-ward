import { clampPercent } from '../utils/helpers';

/**
 * ResourceChart – visual progress bars for hospital resource usage.
 * Accepts an array of { label, used, total, color? } items.
 */
export default function ResourceChart({ items = [] }) {
  return (
    <div className="space-y-5">
      {items.map(({ label, used, total, color }, idx) => {
        const pct = total > 0 ? clampPercent((used / total) * 100) : 0;
        const barColor =
          color || (pct > 85 ? 'from-red-500 to-red-400' : pct > 60 ? 'from-amber-500 to-amber-400' : 'from-emerald-500 to-teal-400');

        return (
          <div key={idx} className="animate-fade-in" style={{ animationDelay: `${idx * 80}ms` }}>
            {/* Label row */}
            <div className="flex items-center justify-between mb-2">
              <span className="text-sm font-medium text-slate-700">{label}</span>
              <span className="text-xs text-slate-500">
                <span className="font-semibold text-slate-700">{used}</span> / {total}{' '}
                <span className={`ml-1 font-bold ${pct > 85 ? 'text-red-600' : pct > 60 ? 'text-amber-600' : 'text-emerald-600'}`}>
                  ({Math.round(pct)}%)
                </span>
              </span>
            </div>

            {/* Bar */}
            <div className="progress-track">
              <div
                className={`progress-fill bg-gradient-to-r ${barColor}`}
                style={{ width: `${pct}%` }}
              />
            </div>
          </div>
        );
      })}
    </div>
  );
}
