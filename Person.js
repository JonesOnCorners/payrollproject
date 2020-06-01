import React from 'react'


const person = (props) => {

     const tableData = {
          padding: '10px'
     }
     return (
          
          <div className="Employee">
          <input type="text" onChange={props.changed} ></input>
          <p > {props.employee_id}</p>         
          <p>{props.employee_name}</p>          
          <p>{props.payroll_month}</p>
          <p>{props.working_hours}</p>
          <p> {props.hourly_rate}</p>
          <p> {props.allowance} </p>
          <p>{props.deductions}</p>
          <p>{props.total_salary}</p>
          
          </div> 
     )

}



export default person