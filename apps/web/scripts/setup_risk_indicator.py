import os

backend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\services\api"
frontend_dir = r"c:\Users\KAVYA\OneDrive\Desktop\Team Titans\educonnect-ai\apps\web"

# --- 1. UPDATE ANALYTICS CONTROLLER FOR RISK CALCULATION ---
ac_path = os.path.join(backend_dir, "controllers", "analyticsController.js")
with open(ac_path, "r", encoding="utf-8") as f: ac_content = f.read()

new_ac_content = """const db = require('../db');

exports.getDashboardStats = (req, res) => {
    const { role, course, semester, id } = req.user;
    
    if (role === 'student') {
        db.all('SELECT * FROM assignments WHERE course = ? AND semester = ?', [course, semester], (err, assignments) => {
            db.all('SELECT * FROM submissions WHERE student_id = ?', [id], (err, submissions) => {
                db.get('SELECT COUNT(*) as materials FROM materials WHERE course = ? AND semester = ?', [course, semester], (err, row3) => {
                    
                    const total_assignments = assignments ? assignments.length : 0;
                    const total_submitted = submissions ? submissions.length : 0;
                    
                    let overdue_count = 0;
                    let graded_count = 0;
                    let total_marks_obtained = 0;
                    let total_marks_possible = 0;

                    if (assignments) {
                        assignments.forEach(a => {
                            const sub = submissions?.find(s => s.assignment_id === a.id);
                            if (!sub && new Date(a.due_date) < new Date()) {
                                overdue_count++;
                            }
                            if (sub && sub.status === 'Graded') {
                                graded_count++;
                                total_marks_obtained += (sub.marks_awarded || 0);
                                total_marks_possible += (a.marks || 0);
                            }
                        });
                    }

                    // Risk Calculation
                    let risk_level = 'Low';
                    let risk_reason = 'Great progress on all tasks.';
                    const completion_rate = total_assignments > 0 ? (total_submitted / total_assignments) * 100 : 0;
                    const grade_percentage = total_marks_possible > 0 ? (total_marks_obtained / total_marks_possible) * 100 : 0;

                    if (total_assignments < 2) {
                        risk_level = 'Insufficient Data';
                        risk_reason = 'Not enough assignments published to determine risk.';
                    } else if (completion_rate < 50 || overdue_count > 2) {
                        risk_level = 'High';
                        risk_reason = `High risk due to ${overdue_count} overdue assignments and ${completion_rate.toFixed(0)}% completion rate.`;
                    } else if (completion_rate < 80 || (graded_count > 0 && grade_percentage < 50)) {
                        risk_level = 'Medium';
                        risk_reason = `Medium risk. Completion is at ${completion_rate.toFixed(0)}%. ${graded_count > 0 ? `Current grade average is ${grade_percentage.toFixed(0)}%.` : ''}`;
                    } else {
                        risk_level = 'Low';
                        risk_reason = `Low risk. You have submitted ${total_submitted} out of ${total_assignments} assignments with ${overdue_count} overdue.`;
                    }

                    res.json({
                        assignments_total: total_assignments,
                        assignments_submitted: total_submitted,
                        assignments_pending: total_assignments - total_submitted,
                        materials_total: row3?.materials || 0,
                        overdue_count,
                        completion_rate,
                        grade_percentage,
                        risk_level,
                        risk_reason,
                        graded_count
                    });
                });
            });
        });
    } else if (role === 'faculty') {
        db.get('SELECT COUNT(*) as total FROM assignments WHERE faculty_id = ?', [id], (err, row1) => {
            db.get('SELECT COUNT(*) as materials FROM materials WHERE faculty_id = ?', [id], (err, row2) => {
                 res.json({
                     assignments_created: row1?.total || 0,
                     materials_uploaded: row2?.materials || 0
                 });
            });
        });
    } else {
        res.json({});
    }
};
"""
with open(ac_path, "w", encoding="utf-8") as f: f.write(new_ac_content)


# --- 2. UPDATE STUDENT DASHBOARD FOR EXPLAINABLE RISK INDICATORS ---
sd_path = os.path.join(frontend_dir, "src/pages/StudentDashboard.tsx")
with open(sd_path, "r", encoding="utf-8") as f: sd_content = f.read()

# Replace the "Recent Announcements" block with the Risk Indicator UI
risk_ui = """         <div className="bg-white rounded-3xl p-8 shadow-sm border border-slate-100 flex flex-col justify-center">
            <h3 className="text-lg font-bold text-slate-900 mb-6 flex items-center gap-2">
              <div className={`w-3 h-3 rounded-full ${stats.risk_level === 'High' ? 'bg-red-500 animate-pulse' : stats.risk_level === 'Medium' ? 'bg-amber-500' : stats.risk_level === 'Low' ? 'bg-emerald-500' : 'bg-slate-300'}`}></div>
              Academic Progress & Risk Indicator
            </h3>
            
            <div className="mb-6">
               <div className="flex justify-between items-end mb-2">
                  <span className="font-bold text-slate-700">Assignment Completion</span>
                  <span className="text-xl font-black text-indigo-600">{stats.completion_rate?.toFixed(0) || 0}%</span>
               </div>
               <div className="w-full bg-slate-100 rounded-full h-3 mb-1 overflow-hidden">
                  <div className="bg-indigo-600 h-3 rounded-full transition-all duration-1000" style={{ width: `${Math.min(100, stats.completion_rate || 0)}%` }}></div>
               </div>
               <p className="text-xs text-slate-500 font-medium">{stats.assignments_submitted} of {stats.assignments_total} submitted</p>
            </div>

            <div className={`p-4 rounded-2xl border ${stats.risk_level === 'High' ? 'bg-red-50 border-red-100' : stats.risk_level === 'Medium' ? 'bg-amber-50 border-amber-100' : stats.risk_level === 'Low' ? 'bg-emerald-50 border-emerald-100' : 'bg-slate-50 border-slate-100'}`}>
               <div className="flex justify-between items-center mb-2">
                  <p className={`font-bold text-sm uppercase tracking-wider ${stats.risk_level === 'High' ? 'text-red-700' : stats.risk_level === 'Medium' ? 'text-amber-700' : stats.risk_level === 'Low' ? 'text-emerald-700' : 'text-slate-600'}`}>
                    Risk Level: {stats.risk_level || 'Calculating...'}
                  </p>
                  {stats.graded_count > 0 && <span className="bg-white px-2 py-1 rounded-md text-xs font-bold shadow-sm">Avg Grade: {stats.grade_percentage?.toFixed(0)}%</span>}
               </div>
               <p className={`text-sm ${stats.risk_level === 'High' ? 'text-red-600' : stats.risk_level === 'Medium' ? 'text-amber-600' : stats.risk_level === 'Low' ? 'text-emerald-600' : 'text-slate-500'}`}>
                  {stats.risk_reason || 'Loading data...'}
               </p>
            </div>
         </div>"""

if "Recent Announcements" in sd_content:
    import re
    # Match the entire div containing "Recent Announcements"
    pattern = r'<div className="bg-white rounded-3xl p-8 shadow-sm border border-slate-100">\s*<h3 className="text-lg font-bold text-slate-900 mb-6 flex items-center gap-2"><Bell className="w-5 h-5 text-amber-500" /> Recent Announcements</h3>.*?</div>\s*</div>\s*</div>'
    sd_content = re.sub(pattern, risk_ui + "\n      </div>\n    </div>", sd_content, flags=re.DOTALL)
    
    # Also add the typing for stats if it helps
    sd_content = sd_content.replace(
        "const [stats, setStats] = useState({ assignments_total: 0, assignments_submitted: 0, assignments_pending: 0, materials_total: 0 });",
        "const [stats, setStats] = useState<any>({ assignments_total: 0, assignments_submitted: 0, assignments_pending: 0, materials_total: 0, risk_level: '', risk_reason: '', completion_rate: 0, grade_percentage: 0, graded_count: 0 });"
    )

    with open(sd_path, "w", encoding="utf-8") as f: f.write(sd_content)

print("Risk indicators implemented.")
