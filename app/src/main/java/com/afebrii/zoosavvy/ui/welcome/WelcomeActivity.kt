package com.afebrii.zoosavvy.ui.welcome

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.afebrii.zoosavvy.databinding.ActivityWelcomeBinding
import com.afebrii.zoosavvy.ui.main.MainActivity
import com.afebrii.zoosavvy.ui.signin.SigninActivity

class WelcomeActivity : AppCompatActivity() {
    private lateinit var binding: ActivityWelcomeBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityWelcomeBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.buttonWelcome.setOnClickListener {
            val i = Intent(this, SigninActivity::class.java)
            startActivity(i)
            finish()
        }
    }
}