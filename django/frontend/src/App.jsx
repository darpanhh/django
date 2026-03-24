import React, { useEffect, useState } from "react";

function App() {
  const [employees,setEmployees] = useState([]);
  const [form,setForm] = useState({name:'',dept:'',salary:'',address:''});
  const [editId,setEditId] = useState(null);

  const API = "http://127.0.0.1:8000/employee/list";

  async function fetchEmployees(){
    const res = await fetch(API);
    const data = await res.json();
    setEmployees(data);
  };

  useEffect(()=>{
    fetchEmployees();
  },[]);

  const handleChange = (e) =>{
    setForm({...form, [e.target.name]:e.target.value})
  }

  const handleSubmit = async (e) =>{
    e.preventDefault();
    if(editId){
      await fetch(`http://127.0.0.1:8000/employee/${editId}/`,{
        method:'PUT',
        headers:{'Content-Type':'application/json'},
        body: JSON.stringify(form)
      });
      setEditId(null);
    }
    else{
      await fetch(API,{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify(form)
      });
    }
    setForm({name: "", dept: "", salary: "", address: "" });
    fetchEmployees();
  }

  const handleDelete = async(id) =>{
    await fetch(`http://127.0.0.1:8000/employee/${id}/`,{method:'DELETE'});
    fetchEmployees();
  }

  const handleEdit = (emp) =>{
    setForm({
      name:emp.name,
      dept:emp.dept,
      salary:emp.salary,
      address:emp.address
    });
    setEditId(emp.id);
  }

  return (
    <div style={{padding:'20px'}}>
      <h2>Employee Management</h2>
      <form onSubmit={handleSubmit}>
      <input name='name' value={form.name} onChange={handleChange} placeholder="Name"/>
      <input name='dept' value={form.dept} onChange={handleChange} placeholder="Department"/>
      <input name='salary' value={form.salary} onChange={handleChange} placeholder="Salary"/>
      <input name='address' value={form.address} onChange={handleChange} placeholder="Address"/>
      <button type="submit">{editId ? "Update":"Add"}</button>
      </form>
      <hr />

      <ul>
        {employees.map((emp)=>(
          <li key={emp.id}>
            {emp.name} - {emp.dept} - {emp.salary} - {emp.address}
            <button onClick={()=>handleEdit(emp)}>Edit</button>
            <button onClick={()=>handleDelete(emp.id)}>Delete</button>
          </li>
        ))
        }
      </ul>

    </div>
  );
}

export default App;
