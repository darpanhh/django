import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [employees, setEmployees] = useState([]);
  const [form, setForm] = useState({ name: "", dept: "", salary: "", address: "" });
  const [editId, setEditId] = useState(null);
  const [loading, setLoading] = useState(false);

  const API = "http://127.0.0.1:8000/employee/list";

  async function fetchEmployees() {
    try {
      setLoading(true);
      const res = await fetch(API);
      const data = await res.json();
      setEmployees(data);
    } catch (error) {
      console.error("Error fetching employees:", error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    fetchEmployees();
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editId) {
        await fetch(`http://127.0.0.1:8000/employee/${editId}/`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(form),
        });
        setEditId(null);
      } else {
        await fetch(API, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(form),
        });
      }
      setForm({ name: "", dept: "", salary: "", address: "" });
      fetchEmployees();
    } catch (error) {
      console.error("Error submitting form:", error);
    }
  };

  const handleDelete = async (id) => {
    try {
      await fetch(`http://127.0.0.1:8000/employee/${id}/`, { method: "DELETE" });
      fetchEmployees();
    } catch (error) {
      console.error("Error deleting employee:", error);
    }
  };

  const handleEdit = (emp) => {
    setForm({
      name: emp.name,
      dept: emp.dept,
      salary: emp.salary,
      address: emp.address,
    });
    setEditId(emp.id);
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleCancel = () => {
    setEditId(null);
    setForm({ name: "", dept: "", salary: "", address: "" });
  };

  return (
    <div className="app-container">
      <div className="app-wrapper">
        {/* Header */}
        <div className="header">
          <h1>👥 Employee Management</h1>
          <p className="header-subtitle">Manage your employee database efficiently</p>
        </div>

        {/* Form Section */}
        <section className="form-section">
          <h3>{editId ? "✏️ Update Employee" : "➕ Add New Employee"}</h3>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <input
                name="name"
                value={form.name}
                onChange={handleChange}
                placeholder="Full Name"
                required
              />
              <input
                name="dept"
                value={form.dept}
                onChange={handleChange}
                placeholder="Department"
                required
              />
              <input
                name="salary"
                value={form.salary}
                onChange={handleChange}
                placeholder="Salary"
                type="number"
                step="0.01"
                required
              />
              <input
                name="address"
                value={form.address}
                onChange={handleChange}
                placeholder="Address"
                required
              />
            </div>
            <div style={{ display: "flex", gap: "1rem" }}>
              <button type="submit" className="btn-submit">
                {editId ? "💾 Update" : "➕ Add Employee"}
              </button>
              {editId && (
                <button
                  type="button"
                  className="btn-submit"
                  onClick={handleCancel}
                  style={{ background: "linear-gradient(135deg, #ef4444, #dc2626)" }}
                >
                  ✕ Cancel
                </button>
              )}
            </div>
          </form>
        </section>

        {/* List Section */}
        <section className="list-section">
          <div className="list-header">
            <h3>📋 Employee List</h3>
            <span className="employee-count">{employees.length} Employees</span>
          </div>

          {loading ? (
            <div style={{ textAlign: "center", padding: "2rem" }}>
              <p>Loading employees...</p>
            </div>
          ) : employees.length === 0 ? (
            <div className="empty-state">
              <p>📭 No employees found. Add your first employee above!</p>
            </div>
          ) : (
            <ul className="employees-list">
              {employees.map((emp) => (
                <li key={emp.id} className="employee-card">
                  <div className="employee-info">
                    <div className="info-row">
                      <span className="info-label">Name</span>
                      <span className="info-value">{emp.name}</span>
                    </div>
                    <div className="info-row">
                      <span className="info-label">Department</span>
                      <span className="info-value">{emp.dept}</span>
                    </div>
                    <div className="info-row">
                      <span className="info-label">Salary</span>
                      <span className="info-value">${parseFloat(emp.salary).toLocaleString()}</span>
                    </div>
                    <div className="info-row">
                      <span className="info-label">Address</span>
                      <span className="info-value">{emp.address}</span>
                    </div>
                  </div>
                  <div className="employee-actions">
                    <button className="btn-edit" onClick={() => handleEdit(emp)}>
                      ✏️ Edit
                    </button>
                    <button className="btn-delete" onClick={() => handleDelete(emp.id)}>
                      🗑️ Delete
                    </button>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </section>
      </div>
    </div>
  );
}

export default App;
