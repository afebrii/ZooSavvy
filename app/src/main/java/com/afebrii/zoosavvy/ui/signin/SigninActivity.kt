package com.afebrii.zoosavvy.ui.signin

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.afebrii.zoosavvy.R
import com.afebrii.zoosavvy.databinding.ActivitySigninBinding
import com.afebrii.zoosavvy.ui.signup.SignupActivity

class SigninActivity : AppCompatActivity() {
    private lateinit var binding: ActivitySigninBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySigninBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.registerHereButton.setOnClickListener {
            val i = Intent(this, SignupActivity::class.java)
            startActivity(i)
            finish()
        }
    }
}