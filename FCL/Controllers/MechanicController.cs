using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using FCL.Helpers;
using FCL.Models;

namespace FCL.Controllers
{
    public class MechanicController : Controller
    {
        // GET: Mechanic
        public ActionResult Index(string lastName = "")
        {
            var mechanics = MechanicHelper.GetMechanicsByLastName(lastName);

            ViewBag.SearchString = lastName;

            return View(mechanics);
        }

        // GET: Mechanic/Details/5
        public ActionResult Details(int id)
        {
            return View();
        }

        // GET: Mechanic/Create
        public ActionResult Create()
        {
            return View(new Mechanic());
        }

        // POST: Mechanic/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(string firstName, string lastName)
        {
            try
            {
                MechanicHelper.InsertNewMechanic(firstName, lastName);

                return RedirectToAction(nameof(Index));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());

                return View();
            }
        }

        // GET: Mechanic/Edit/5
        public ActionResult Edit(int id)
        {
            return View();
        }

        // POST: Mechanic/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(int id, IFormCollection collection)
        {
            try
            {
                // TODO: Add update logic here

                return RedirectToAction(nameof(Index));
            }
            catch
            {
                return View();
            }
        }

        // GET: Mechanic/Delete/5
        public ActionResult Delete(int id)
        {
            return View();
        }

        // POST: Mechanic/Delete/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Delete(int id, IFormCollection collection)
        {
            try
            {
                // TODO: Add delete logic here

                return RedirectToAction(nameof(Index));
            }
            catch
            {
                return View();
            }
        }
    }
}