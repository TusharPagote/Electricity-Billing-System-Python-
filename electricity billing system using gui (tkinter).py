import imp
from tempfile import tempdir
from tkinter import *
import math
import random



class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1080x780+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color, fg="white",
                      font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        ##################### VARIABLES #####################
        # CUSTOMER
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # APPPLIENCES
        self.bulb1 = IntVar()
        self.bulb2 = IntVar()
        self.bulb3 = IntVar()
        self.computer = IntVar()
        self.fan = IntVar()
        self.cooler = IntVar()
        self.ac = IntVar()

        self.bulb1_time = IntVar()
        self.bulb2_time = IntVar()
        self.bulb3_time = IntVar()
        self.computer_time = IntVar()
        self.fan_time = IntVar()
        self.cooler_time = IntVar()
        self.ac_time = IntVar()

        # DAILY NEEDS
        self.tv = IntVar()
        self.geyser = IntVar()
        self.refrigerator = IntVar()
        self.wm = IntVar()
        self.oven = IntVar()
        self.induction = IntVar()
        self.heater = IntVar()

        self.tv_time = IntVar()
        self.geyser_time = IntVar()
        self.refrigerator_time = IntVar()
        self.wm_time = IntVar()
        self.oven_time = IntVar()
        self.induction_time = IntVar()
        self.heater_time = IntVar()

        # OTHER appliances
        self.wp = IntVar()
        self.machine = IntVar()
        self.mixture = IntVar()
        self.vc = IntVar()
        self.cm = IntVar()
        self.speakers = IntVar()
        self.dw = IntVar()

        self.wp_time = IntVar()
        self.machine_time = IntVar()
        self.mixture_time = IntVar()
        self.vc_time = IntVar()
        self.cm_time = IntVar()
        self.speakers_time = IntVar()
        self.dw_time = IntVar()

        # TOTAL FRAME
        self.appliances_power = DoubleVar()
        self.daily_needs_power = DoubleVar()
        self.other_appliances_power = DoubleVar()

        self.appliances_units = DoubleVar()
        self.daily_needs_units = DoubleVar()
        self.other_appliances_units = DoubleVar()
        self.total_units = DoubleVar()
        self.total_power = DoubleVar()
        self.pay_amount = DoubleVar()
        self.fixed_charge = DoubleVar()
        self.total_amount = DoubleVar()

        self.search_bill = StringVar()

        #####################  Customer Detail Frame  #####################
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"),
                        fg="gold",
                        bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        c_name_label = Label(F1, text="Customer Name", bg=bg_color, fg='white',
                             font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        c_name_txt = Entry(F1, width=20, textvariable=self.c_name, font='arial 15', bd=7, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=5)

        c_phone_label = Label(F1, text="Phone No.", bg=bg_color, fg='white',
                              font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        c_phone_txt = Entry(F1, width=20, textvariable=self.c_phone, font='arial 15', bd=7, relief=SUNKEN).grid(
            row=0, column=3, padx=10, pady=5)

        c_bill_label = Label(F1, text="Customer Bill", bg=bg_color, fg='white',
                             font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=20, textvariable=self.search_bill, font='arial 15', bd=7, relief=SUNKEN).grid(
            row=0, column=5, padx=10, pady=5)

        bill_btn = Button(F1, text="Search", width=5, bd=7, font="arial 12 bold").grid(row=0, column=6, padx=10,
                                                                                       pady=10)

        ##################### appliances #############################
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Appliances", font=("times new roman", 15, "bold"),
                        fg="gold",
                        bg=bg_color)
        F2.place(x=0, y=180, width=355, height=465)

        quentity_label = Label(F2, text="Quentity", font=("times new roman", 11),
                               bg=bg_color, fg="gray").grid(row=0, column=1, padx=7, pady=10, sticky="w")

        duration_label = Label(F2, text="Duration", font=("times new roman", 11),
                               bg=bg_color, fg="gray").grid(row=0, column=2, padx=7, pady=10, sticky="w")

        bulb_1_label = Label(F2, text="10W Bulb              ", font=("times new roman", 14, "bold"),
                             bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        bulb_1_txt = Entry(F2, width=5, textvariable=self.bulb1, font=("times new roman", 14, "bold"), bd=5,
                           relief=SUNKEN).grid(row=1, column=1,
                                               padx=7, pady=10)
        bulb_1_time = Entry(F2, width=5, textvariable=self.bulb1_time, font=("times new roman", 14, "bold"), bd=5,
                            relief=SUNKEN).grid(row=1, column=2,
                                                padx=5, pady=10)

        bulb_2_label = Label(F2, text="60W Bulb", font=("times new roman", 14, "bold"),
                             bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        bulb_2_txt = Entry(F2, width=5, textvariable=self.bulb2, font=("times new roman", 14, "bold"), bd=5,
                           relief=SUNKEN).grid(row=2,
                                               column=1,
                                               padx=10,
                                               pady=10)
        bulb_2_time = Entry(F2, width=5, textvariable=self.bulb2_time, font=("times new roman", 14, "bold"), bd=5,
                            relief=SUNKEN).grid(row=2,
                                                column=2,
                                                padx=10,
                                                pady=10)

        bulb_3_label = Label(F2, text="100W Bulb", font=("times new roman", 14, "bold"), bg=bg_color,
                             fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        bulb_3_txt = Entry(F2, width=5, textvariable=self.bulb3, font=("times new roman", 14, "bold"), bd=5,
                           relief=SUNKEN).grid(row=3,
                                               column=1,
                                               padx=10,
                                               pady=10)
        bulb_3_time = Entry(F2, width=5, textvariable=self.bulb3_time, font=("times new roman", 14, "bold"), bd=5,
                            relief=SUNKEN).grid(row=3,
                                                column=2,
                                                padx=10,
                                                pady=10)

        computer_label = Label(F2, text="Computer", font=("times new roman", 14, "bold"), bg=bg_color,
                               fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        computer_txt = Entry(F2, width=5, textvariable=self.computer, font=("times new roman", 14, "bold"), bd=5,
                             relief=SUNKEN).grid(row=4,
                                                 column=1,
                                                 padx=10,
                                                 pady=10)
        computer_time = Entry(F2, width=5, textvariable=self.computer_time, font=("times new roman", 14, "bold"), bd=5,
                              relief=SUNKEN).grid(row=4,
                                                  column=2,
                                                  padx=10,
                                                  pady=10)

        fan_label = Label(F2, text="Fan", font=("times new roman", 14, "bold"), bg=bg_color,
                          fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        fan_txt = Entry(F2, width=5, textvariable=self.fan, font=("times new roman", 14, "bold"), bd=5,
                        relief=SUNKEN).grid(row=5,
                                            column=1,
                                            padx=10,
                                            pady=10)
        fan_time = Entry(F2, width=5, textvariable=self.fan_time, font=("times new roman", 14, "bold"), bd=5,
                         relief=SUNKEN).grid(row=5,
                                             column=2,
                                             padx=10,
                                             pady=10)

        cooler_label = Label(F2, text="Cooler", font=("times new roman", 14, "bold"), bg=bg_color,
                             fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        cooler_txt = Entry(F2, width=5, textvariable=self.cooler, font=("times new roman", 14, "bold"), bd=5,
                           relief=SUNKEN).grid(row=6,
                                               column=1,
                                               padx=10,
                                               pady=10)
        cooler_time = Entry(F2, width=5, textvariable=self.cooler_time, font=("times new roman", 14, "bold"), bd=5,
                            relief=SUNKEN).grid(row=6,
                                                column=2,
                                                padx=10,
                                                pady=10)

        ac_label = Label(F2, text="AC", font=("times new roman", 14, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        ac_txt = Entry(F2, width=5, textvariable=self.ac, font=("times new roman", 14, "bold"), bd=5,
                       relief=SUNKEN).grid(row=7,
                                           column=1,
                                           padx=10,
                                           pady=10)
        ac_time = Entry(F2, width=5, textvariable=self.ac_time, font=("times new roman", 14, "bold"), bd=5,
                        relief=SUNKEN).grid(row=7,
                                            column=2,
                                            padx=10,
                                            pady=10)

        ##################### DIALY NEEDS #############################
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Daily Needs", font=("times new roman", 15, "bold"),
                        fg="gold",
                        bg=bg_color)
        F3.place(x=355, y=180, width=355, height=465)

        quentity_label = Label(F3, text="Quentity", font=("times new roman", 11),
                               bg=bg_color, fg="gray").grid(row=0, column=1, padx=7, pady=10, sticky="w")

        duration_label = Label(F3, text="Duration", font=("times new roman", 11),
                               bg=bg_color, fg="gray").grid(row=0, column=2, padx=7, pady=10, sticky="w")

        tv_label = Label(F3, text="TV", font=("times new roman", 14, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tv_txt = Entry(F3, width=5, textvariable=self.tv, font=("times new roman", 14, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1,
                                           padx=10, pady=10)
        tv_time = Entry(F3, width=5, textvariable=self.tv_time, font=("times new roman", 14, "bold"), bd=5,
                        relief=SUNKEN).grid(row=1, column=2,
                                            padx=10, pady=10)

        geyser_label = Label(F3, text="Geyser", font=("times new roman", 14, "bold"),
                             bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        geyser_txt = Entry(F3, width=5, textvariable=self.geyser, font=("times new roman", 14, "bold"), bd=5,
                           relief=SUNKEN).grid(row=2,
                                               column=1,
                                               padx=10,
                                               pady=10)
        geyser_time = Entry(F3, width=5, textvariable=self.geyser_time, font=("times new roman", 14, "bold"), bd=5,
                            relief=SUNKEN).grid(row=2,
                                                column=2,
                                                padx=10,
                                                pady=10)

        refrigerator_label = Label(F3, text="Refrigerator", font=("times new roman", 14, "bold"), bg=bg_color,
                                   fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        refrigerator_txt = Entry(F3, width=5, textvariable=self.refrigerator, font=("times new roman", 14, "bold"),
                                 bd=5, relief=SUNKEN).grid(row=3,
                                                           column=1,
                                                           padx=10,
                                                           pady=10)
        refrigerator_time = Entry(F3, width=5, textvariable=self.refrigerator_time,
                                  font=("times new roman", 14, "bold"),
                                  bd=5, relief=SUNKEN).grid(row=3,
                                                            column=2,
                                                            padx=10,
                                                            pady=10)

        wm_label = Label(F3, text="Washing Machine", font=("times new roman", 14, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        wm_txt = Entry(F3, width=5, textvariable=self.wm, font=("times new roman", 14, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4,
                                           column=1,
                                           padx=10,
                                           pady=10)
        wm_time = Entry(F3, width=5, textvariable=self.wm_time, font=("times new roman", 14, "bold"), bd=5,
                        relief=SUNKEN).grid(row=4,
                                            column=2,
                                            padx=10,
                                            pady=10)

        oven_label = Label(F3, text="Oven", font=("times new roman", 14, "bold"), bg=bg_color,
                           fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        oven_txt = Entry(F3, width=5, textvariable=self.oven, font=("times new roman", 14, "bold"), bd=5,
                         relief=SUNKEN).grid(row=5,
                                             column=1,
                                             padx=10,
                                             pady=10)
        oven_time = Entry(F3, width=5, textvariable=self.oven_time, font=("times new roman", 14, "bold"), bd=5,
                          relief=SUNKEN).grid(row=5,
                                              column=2,
                                              padx=10,
                                              pady=10)

        induction_label = Label(F3, text="Induction", font=("times new roman", 14, "bold"), bg=bg_color,
                                fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        induction_txt = Entry(F3, width=5, textvariable=self.induction, font=("times new roman", 14, "bold"), bd=5,
                              relief=SUNKEN).grid(row=6,
                                                  column=1,
                                                  padx=10,
                                                  pady=10)
        induction_time = Entry(F3, width=5, textvariable=self.induction_time, font=("times new roman", 14, "bold"),
                               bd=5,
                               relief=SUNKEN).grid(row=6,
                                                   column=2,
                                                   padx=10,
                                                   pady=10)

        heater_label = Label(F3, text="Heater", font=("times new roman", 14, "bold"), bg=bg_color,
                             fg="lightgreen").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        heater_txt = Entry(F3, width=5, textvariable=self.heater, font=("times new roman", 14, "bold"), bd=5,
                           relief=SUNKEN).grid(row=7,
                                               column=1,
                                               padx=10,
                                               pady=10)
        heater_time = Entry(F3, width=5, textvariable=self.heater_time, font=("times new roman", 14, "bold"), bd=5,
                            relief=SUNKEN).grid(row=7,
                                                column=2,
                                                padx=10,
                                                pady=10)

        ##################### OTHER APPLIENCES #############################

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Other Appliances", font=("times new roman", 15, "bold"),
                        fg="gold",
                        bg=bg_color)
        F4.place(x=710, y=180, width=355, height=465)

        quentity_label = Label(F4, text="Quentity", font=("times new roman", 11),
                               bg=bg_color, fg="gray").grid(row=0, column=1, padx=7, pady=10, sticky="w")

        duration_label = Label(F4, text="Duration", font=("times new roman", 11),
                               bg=bg_color, fg="gray").grid(row=0, column=2, padx=7, pady=10, sticky="w")

        wp_label = Label(F4, text="Water Pump", font=("times new roman", 14, "bold"),
                         bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        wp_txt = Entry(F4, width=5, textvariable=self.wp, font=("times new roman", 14, "bold"), bd=5,
                       relief=SUNKEN).grid(row=1, column=1,
                                           padx=10, pady=10)
        wp_time = Entry(F4, width=5, textvariable=self.wp_time, font=("times new roman", 14, "bold"), bd=5,
                        relief=SUNKEN).grid(row=1, column=2,
                                            padx=10, pady=10)

        machine_label = Label(F4, text="Machine", font=("times new roman", 14, "bold"),
                              bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        machine_txt = Entry(F4, width=5, textvariable=self.machine, font=("times new roman", 14, "bold"), bd=5,
                            relief=SUNKEN).grid(row=2,
                                                column=1,
                                                padx=10,
                                                pady=10)
        machine_time = Entry(F4, width=5, textvariable=self.machine_time, font=("times new roman", 14, "bold"), bd=5,
                             relief=SUNKEN).grid(row=2,
                                                 column=2,
                                                 padx=10,
                                                 pady=10)

        mixture_label = Label(F4, text="Mixture", font=("times new roman", 14, "bold"), bg=bg_color,
                              fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        mixture_txt = Entry(F4, width=5, textvariable=self.mixture, font=("times new roman", 14, "bold"), bd=5,
                            relief=SUNKEN).grid(row=3,
                                                column=1,
                                                padx=10,
                                                pady=10)
        mixture_time = Entry(F4, width=5, textvariable=self.mixture_time, font=("times new roman", 14, "bold"), bd=5,
                             relief=SUNKEN).grid(row=3,
                                                 column=2,
                                                 padx=10,
                                                 pady=10)

        vc_label = Label(F4, text="Vaccume Cleaner", font=("times new roman", 14, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        vc_txt = Entry(F4, width=5, textvariable=self.vc, font=("times new roman", 14, "bold"), bd=5,
                       relief=SUNKEN).grid(row=4,
                                           column=1,
                                           padx=10,
                                           pady=10)
        vc_time = Entry(F4, width=5, textvariable=self.vc_time, font=("times new roman", 14, "bold"), bd=5,
                        relief=SUNKEN).grid(row=4,
                                            column=2,
                                            padx=10,
                                            pady=10)

        cm_label = Label(F4, text="Coffee Maker", font=("times new roman", 14, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        cm_txt = Entry(F4, width=5, textvariable=self.cm, font=("times new roman", 14, "bold"), bd=5,
                       relief=SUNKEN).grid(row=5,
                                           column=1,
                                           padx=10,
                                           pady=10)
        cm_time = Entry(F4, width=5, textvariable=self.cm_time, font=("times new roman", 14, "bold"), bd=5,
                        relief=SUNKEN).grid(row=5,
                                            column=2,
                                            padx=10,
                                            pady=10)

        speakers_label = Label(F4, text="Speakers", font=("times new roman", 14, "bold"), bg=bg_color,
                               fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        speakers_txt = Entry(F4, width=5, textvariable=self.speakers, font=("times new roman", 14, "bold"), bd=5,
                             relief=SUNKEN).grid(row=6,
                                                 column=1,
                                                 padx=10,
                                                 pady=10)
        speakers_time = Entry(F4, width=5, textvariable=self.speakers_time, font=("times new roman", 14, "bold"), bd=5,
                              relief=SUNKEN).grid(row=6,
                                                  column=2,
                                                  padx=10,
                                                  pady=10)

        dw_label = Label(F4, text="Dish Washer", font=("times new roman", 14, "bold"), bg=bg_color,
                         fg="lightgreen").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        dw_txt = Entry(F4, width=5, textvariable=self.dw, font=("times new roman", 14, "bold"), bd=5,
                       relief=SUNKEN).grid(row=7,
                                           column=1,
                                           padx=10,
                                           pady=10)
        dw_time = Entry(F4, width=5, textvariable=self.dw_time, font=("times new roman", 14, "bold"), bd=5,
                        relief=SUNKEN).grid(row=7,
                                            column=2,
                                            padx=10,
                                            pady=10)

        ##################### BILL AREA #############################
        F5 = LabelFrame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1065, y=180, width=465, height=465)
        bill_title = Label(
            F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.textarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        ##################### BUTTONS #############################
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg="gold",
                        bg=bg_color)
        F6.place(x=0, y=645, relwidth=1, height=150)
        m1_label = Label(F6, text="Appliences Power", bg=bg_color, fg="lightgreen",
                         font=("times new roman", 14, "bold")).grid(row=0, column=0,
                                                                    padx=20, pady=1,
                                                                    sticky="w")
        m1_text = Entry(F6, width=18, textvariable=self.appliances_power, font="arial 10 bold", bd=7,
                        relief=SUNKEN).grid(row=0, column=1, padx=20, pady=1)

        m2_label = Label(F6, text="Dialy Needs Power", bg=bg_color, fg="lightgreen",
                         font=("times new roman", 14, "bold")).grid(row=1, column=0,
                                                                    padx=20, pady=1,
                                                                    sticky="w")
        m2_text = Entry(F6, width=18, textvariable=self.daily_needs_power, font="arial 10 bold", bd=7,
                        relief=SUNKEN).grid(row=1, column=1, padx=20, pady=1)

        m3_label = Label(F6, text="Other Appliances Power", bg=bg_color, fg="lightgreen",
                         font=("times new roman", 14, "bold")).grid(row=2, column=0,
                                                                    padx=20, pady=1,
                                                                    sticky="w")
        m3_text = Entry(F6, width=18, textvariable=self.other_appliances_power, font="arial 10 bold", bd=7,
                        relief=SUNKEN).grid(row=2, column=1, padx=20, pady=1)

        c1_label = Label(F6, text="Appliences Units", bg=bg_color, fg="lightgreen",
                         font=("times new roman", 14, "bold")).grid(row=0, column=3,
                                                                    padx=20, pady=1,
                                                                    sticky="w")
        c1_text = Entry(F6, width=18, textvariable=self.appliances_units, font="arial 10 bold", bd=7,
                        relief=SUNKEN).grid(row=0, column=4, padx=20, pady=1)

        c2_label = Label(F6, text="Daily Needs Units", bg=bg_color, fg="lightgreen",
                         font=("times new roman", 14, "bold")).grid(row=1, column=3,
                                                                    padx=20, pady=1,
                                                                    sticky="w")
        c2_text = Entry(F6, width=18, textvariable=self.daily_needs_units, font="arial 10 bold", bd=7,
                        relief=SUNKEN).grid(row=1, column=4, padx=20, pady=1)

        c3_label = Label(F6, text="Other Appliences Units", bg=bg_color, fg="lightgreen",
                         font=("times new roman", 14, "bold")).grid(row=2, column=3,
                                                                    padx=20, pady=1,
                                                                    sticky="w")
        c3_text = Entry(F6, width=18, textvariable=self.other_appliances_units, font="arial 10 bold", bd=7,
                        relief=SUNKEN).grid(row=2, column=4, padx=20, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=880, width=630, height=100)

        total_button = Button(btn_F, text="Total", command=self.total, bg="cadetblue", fg="white", pady=15, width=13,
                              bd=5,
                              font="arial 12 bold").grid(row=0, column=0, pady=5, padx=5)
        generate_bill_button = Button(btn_F, text="Generate Bill", command=self.welcome_bill, bg="cadetblue",
                                      fg="white", pady=15, width=13, bd=5,
                                      font="arial 12 bold").grid(row=0, column=1, pady=5, padx=5)
        clear_button = Button(btn_F, text="Clear", command=self.clear_screen, bg="cadetblue", fg="white", pady=15, width=13, bd=5,
                              font="arial 12 bold").grid(row=0, column=2, pady=5, padx=5)
        exit_button = Button(btn_F, text="Exit", command=exit, bg="cadetblue", fg="white", pady=15, width=13, bd=5,
                             font="arial 12 bold").grid(row=0, column=3, pady=5, padx=5)
        self.welcome_bill()

    def calculate_units(self, power):
        temp1 = 0.0
        temp1 = 0.0
        units = 0.0
        while (power > 1000):
            temp1 = temp1 + 1
            power = power - 1000
        else:
            temp2 = power / 1000
        units = temp1 + temp2
        # units = round(units, 2)
        return units

    def total(self):
        self.total_appliances_cost = (
            self.bulb1.get() * 10 * self.bulb1_time.get() +
            self.bulb2.get() * 60 * self.bulb2_time.get() +
            self.bulb3.get() * 100 * self.bulb3_time.get() +
            self.computer.get() * 150 * self.computer_time.get() +
            self.fan.get() * 80 * self.fan_time.get() +
            self.cooler.get() * 225 * self.cooler_time.get() +
            self.ac.get() * 2000 * self.ac_time.get()
        )
        # self.appliances_power.set(round(self.total_appliances_cost, 2))
        self.appliances_power.set(self.total_appliances_cost)

        self.appliances_units.set(
            self.calculate_units(self.total_appliances_cost))

        self.total_daily_needs_cost = (
            self.tv.get() * 100 * self.tv_time.get() +
            self.geyser.get() * 2000 * self.geyser_time.get() +
            self.refrigerator.get() * 700 * self.refrigerator_time.get() +
            self.wm.get() * 2500 * self.wm_time.get() +
            self.oven.get() * 1200 * self.oven_time.get() +
            self.induction.get() * 1500 * self.induction_time.get() +
            self.heater.get() * 2250 * self.heater_time.get()
        )
        # self.daily_needs_power.set(round(self.total_daily_needs_cost, 2))
        self.daily_needs_power.set(self.total_daily_needs_cost)
        self.daily_needs_units.set(
            self.calculate_units(self.total_daily_needs_cost))

        self.total_other_appliances_cost = (
            self.wp.get() * 750 * self.wp_time.get() +
            self.machine.get() * 100 * self.machine_time.get() +
            self.mixture.get() * 750 * self.mixture_time.get() +
            self.vc.get() * 1400 * self.vc_time.get() +
            self.cm.get() * 1000 * self.cm_time.get() +
            self.speakers.get() * 30 * self.speakers_time.get() +
            self.dw.get() * 800 * self.dw_time.get()
        )
        # self.other_appliances_power.set(
        #     round(self.total_other_appliances_cost, 2))
        self.other_appliances_power.set(
            self.total_other_appliances_cost)
        self.other_appliances_units.set(
            self.calculate_units(self.total_other_appliances_cost))
        # self.total_power = round((self.appliances_power.get() + self.daily_needs_power.get() +
        #                           self.other_appliances_power.get()), 2)
        # self.total_units = round((self.appliances_units.get() + self.daily_needs_units.get() +
        #                           self.other_appliances_units.get()), 2)
        self.total_power = (self.appliances_power.get() + self.daily_needs_power.get() +
                            self.other_appliances_power.get())
        self.total_units = (self.appliances_units.get() + self.daily_needs_units.get() +
                            self.other_appliances_units.get())

    def bill_area(self):
        if (self.total_units <= 100):

            return self.total_units * 10

        elif (self.total_units <= 200):

            return ((100 * 10) +
                    (self.total_units - 100) * 15)

        elif (self.total_units <= 300):

            return ((100 * 10) +
                    (100 * 15) +
                    (self.total_units - 200) * 20)

        elif (self.total_units > 300):

            return ((100 * 10) +
                    (100 * 15) +
                    (100 * 20) +
                    (self.total_units - 300) * 25)

        return 0

    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(END, "\t\tWelcome to Billing Software")
        if self.c_name.get():
            self.textarea.insert(
                END, f"\n\n\tBill Number   : {self.bill_no.get()}")
            self.textarea.insert(
                END, f"\n\tCustomer Name : {self.c_name.get()}")
            self.textarea.insert(
                END, f"\n\tPhone No.     : {self.c_phone.get()}")
            self.textarea.insert(
                END, f"\n=====================================================")
            self.textarea.insert(
                END, f"\n\tProducts\t\tPower Used (W)\t\tUnits Used")
            self.textarea.insert(
                END, f"\n=====================================================")
            if self.appliances_units.get() != 0:
                self.textarea.insert(
                    END, f"\n       Appliences       \t\t{self.appliances_power.get()}\t\t\t{self.appliances_units.get()}")
            if self.daily_needs_units.get() != 0:
                self.textarea.insert(
                    END, f"\n       Daily Needs      \t\t{self.daily_needs_power.get()}\t\t\t{self.daily_needs_units.get()}")
            if self.other_appliances_units.get() != 0:
                self.textarea.insert(
                    END, f"\n       Other Appliences \t\t{self.other_appliances_power.get()}\t\t\t{self.other_appliances_units.get()}")
            self.textarea.insert(
                END, f"\n=====================================================")

            self.total_amount = self.bill_area()
            self.textarea.insert(
                END, f"\n\tTotal    \t\t{self.total_amount}\t\t{self.total_units}")

    def clear_screen(self):
        # CUSTOMER
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")

        # APPPLIENCES
        self.bulb1.set(0)
        self.bulb2.set(0)
        self.bulb3.set(0)
        self.computer.set(0)
        self.fan.set(0)
        self.cooler.set(0)
        self.ac.set(0)

        self.bulb1_time.set(0)
        self.bulb2_time.set(0)
        self.bulb3_time.set(0)
        self.computer_time.set(0)
        self.fan_time.set(0)
        self.cooler_time.set(0)
        self.ac_time.set(0)

        # DAILY NEEDS
        self.tv.set(0)
        self.geyser.set(0)
        self.refrigerator.set(0)
        self.wm.set(0)
        self.oven.set(0)
        self.induction.set(0)
        self.heater.set(0)

        self.tv_time.set(0)
        self.geyser_time.set(0)
        self.refrigerator_time.set(0)
        self.wm_time.set(0)
        self.oven_time.set(0)
        self.induction_time.set(0)
        self.heater_time.set(0)

        # OTHER appliances
        self.wp.set(0)
        self.machine.set(0)
        self.mixture.set(0)
        self.vc.set(0)
        self.cm.set(0)
        self.speakers.set(0)
        self.dw.set(0)

        self.wp_time.set(0)
        self.machine_time.set(0)
        self.mixture_time.set(0)
        self.vc_time.set(0)
        self.cm_time.set(0)
        self.speakers_time.set(0)
        self.dw_time.set(0)

        # TOTAL FRAME
        self.appliances_power.set(0.0)
        self.daily_needs_power.set(0.0)
        self.other_appliances_power.set(0.0)

        self.appliances_units.set(0.0)
        self.daily_needs_units.set(0.0)
        self.other_appliances_units.set(0.0)
        self.total_units.set(0.0)
        self.total_power.set(0.0)
        self.pay_amount.set(0.0)
        self.fixed_charge.set(0.0)
        self.total_amount.set(0.0)

        self.search_bill.set("")


root = Tk()
obj = Bill_App(root)
root.mainloop()
