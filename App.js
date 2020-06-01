import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Person from './Person/Person';
import UserOutput from './UserOutput/UserOutput';
import UserInput from './UserInput/UserInput';

class App extends Component {

  state = {
    employees: [
      {
        id: 'abc',
        employee_id: 1,
        employee_name: 'Jaydeep Karale',
        payroll_month: 'May-2020',
        working_hours: 10,
        hourly_rate: 10,
        allowance: 100,
        deductions: 10,
        total_salary: 90
      },
      {
        id: 'def',
        employee_id: 2,
        employee_name: 'Vishal Chavan',
        payroll_month: 'May-2020',
        working_hours: 110,
        hourly_rate: 110,
        allowance: 1000,
        deductions: 100,
        total_salary: 90
      }
    ],
    userName: 'SuperFundoo',
    showEmployee: false,
  }




  toggleHandler = () => {
    const toggleLocal = this.state.showEmployee
    //console.log(t)
    this.setState({ showEmployee: !toggleLocal })
  }

  deleteEmployeeHandler = (employeeIndex) => {
    const employees = [...this.state.employees]
    employees.splice(employeeIndex, 1)
    this.setState({ employees: employees })
  }


  userNameChangeHandler = (event, employeeId) => {

    const employeeIndex = this.state.employees.findIndex(p => {
      return p.employee_id === employeeId
    })


    const employee = {
      ...this.state.employees[employeeIndex]


    }
    console.log("SELECTED-->",employee)
    
    employee.employee_name = event.target.value
    const employees = [...this.state.employees]
    employees[employeeId] = employee

    console.log("FINAL-->",employees)

    

    this.setState({ employees: employees })
  }


  render() {
    const styleMedia = {
      margin: 'auto',
      padding: '10px',
      width: '50%',
      border: '5px solid black'
    }

    let employees = null;

    if (this.state.showEmployee) {
      employees = (
        <div >
          {this.state.employees.map((employees,index) => {
            return <Person
              employee_id={employees.employee_id}
              employee_name={employees.employee_name} value={employees.employee_name}
              payroll_month={employees.payroll_month}
              working_hours={employees.working_hours}
              hourly_rate={employees.hourly_rate}
              allowance={employees.allowance}
              deductions={employees.deductions}
              total_salary={employees.total_salary}
              changed={(event) => this.userNameChangeHandler(event, employees.employee_id)}
            />
          })}
        </div>

      )
    }

    const styleBtn = {
      margin: 'auto',
      width: '50%',
      padding: '10px'
    }

    const tableStyle = {
      border: '5px solid black',
      margin: 'auto',
    }
    const tableRow = {
      padding: '10px'
    }

    const tableData = {
      padding: '10px'
    }
    return (
      <div>
        <button style={styleBtn} onClick={this.toggleHandler} >Click me</button>

        <table style={tableStyle}>
          <caption><b>PAYROLL CHART</b></caption>
          <thead>
            <tr style={tableRow}>
              <th>Employee Id</th>
              <th>Employee Name</th>
              <th>Payroll Month</th>
              <th>Working Hours</th>
              <th>Hourly Rate</th>
              <th>Allowance</th>
              <th>Deductions</th>
              <th>Net Pay</th>
            </tr>
          </thead>
        </table>
        {employees}
      </div>
    );
  }
}

export default App;


// <div className="App">
//         <header className="App-header">
//           <img src={logo} className="App-logo" alt="logo" />
//           <h1 className="App-title">Welcome to React</h1>
//         </header>
//         <p className="App-intro">
//           To get started, edit <code>src/App.js</code> and save to reload.
//         </p>
//       </div>