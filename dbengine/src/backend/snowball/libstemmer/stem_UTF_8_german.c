/* Generated by Snowball 2.2.0 - https://snowballstem.org/ */

#include "header.h"

#ifdef __cplusplus
extern "C" {
#endif
extern int german_UTF_8_stem(struct SN_env * z);
#ifdef __cplusplus
}
#endif
static int r_standard_suffix(struct SN_env * z);
static int r_R2(struct SN_env * z);
static int r_R1(struct SN_env * z);
static int r_mark_regions(struct SN_env * z);
static int r_postlude(struct SN_env * z);
static int r_prelude(struct SN_env * z);
#ifdef __cplusplus
extern "C" {
#endif


extern struct SN_env * german_UTF_8_create_env(void);
extern void german_UTF_8_close_env(struct SN_env * z);


#ifdef __cplusplus
}
#endif
static const symbol s_0_1[1] = { 'U' };
static const symbol s_0_2[1] = { 'Y' };
static const symbol s_0_3[2] = { 0xC3, 0xA4 };
static const symbol s_0_4[2] = { 0xC3, 0xB6 };
static const symbol s_0_5[2] = { 0xC3, 0xBC };

static const struct among a_0[6] =
{
{ 0, 0, -1, 5, 0},
{ 1, s_0_1, 0, 2, 0},
{ 1, s_0_2, 0, 1, 0},
{ 2, s_0_3, 0, 3, 0},
{ 2, s_0_4, 0, 4, 0},
{ 2, s_0_5, 0, 2, 0}
};

static const symbol s_1_0[1] = { 'e' };
static const symbol s_1_1[2] = { 'e', 'm' };
static const symbol s_1_2[2] = { 'e', 'n' };
static const symbol s_1_3[3] = { 'e', 'r', 'n' };
static const symbol s_1_4[2] = { 'e', 'r' };
static const symbol s_1_5[1] = { 's' };
static const symbol s_1_6[2] = { 'e', 's' };

static const struct among a_1[7] =
{
{ 1, s_1_0, -1, 2, 0},
{ 2, s_1_1, -1, 1, 0},
{ 2, s_1_2, -1, 2, 0},
{ 3, s_1_3, -1, 1, 0},
{ 2, s_1_4, -1, 1, 0},
{ 1, s_1_5, -1, 3, 0},
{ 2, s_1_6, 5, 2, 0}
};

static const symbol s_2_0[2] = { 'e', 'n' };
static const symbol s_2_1[2] = { 'e', 'r' };
static const symbol s_2_2[2] = { 's', 't' };
static const symbol s_2_3[3] = { 'e', 's', 't' };

static const struct among a_2[4] =
{
{ 2, s_2_0, -1, 1, 0},
{ 2, s_2_1, -1, 1, 0},
{ 2, s_2_2, -1, 2, 0},
{ 3, s_2_3, 2, 1, 0}
};

static const symbol s_3_0[2] = { 'i', 'g' };
static const symbol s_3_1[4] = { 'l', 'i', 'c', 'h' };

static const struct among a_3[2] =
{
{ 2, s_3_0, -1, 1, 0},
{ 4, s_3_1, -1, 1, 0}
};

static const symbol s_4_0[3] = { 'e', 'n', 'd' };
static const symbol s_4_1[2] = { 'i', 'g' };
static const symbol s_4_2[3] = { 'u', 'n', 'g' };
static const symbol s_4_3[4] = { 'l', 'i', 'c', 'h' };
static const symbol s_4_4[4] = { 'i', 's', 'c', 'h' };
static const symbol s_4_5[2] = { 'i', 'k' };
static const symbol s_4_6[4] = { 'h', 'e', 'i', 't' };
static const symbol s_4_7[4] = { 'k', 'e', 'i', 't' };

static const struct among a_4[8] =
{
{ 3, s_4_0, -1, 1, 0},
{ 2, s_4_1, -1, 2, 0},
{ 3, s_4_2, -1, 1, 0},
{ 4, s_4_3, -1, 3, 0},
{ 4, s_4_4, -1, 2, 0},
{ 2, s_4_5, -1, 2, 0},
{ 4, s_4_6, -1, 3, 0},
{ 4, s_4_7, -1, 4, 0}
};

static const unsigned char g_v[] = { 17, 65, 16, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 32, 8 };

static const unsigned char g_s_ending[] = { 117, 30, 5 };

static const unsigned char g_st_ending[] = { 117, 30, 4 };

static const symbol s_0[] = { 0xC3, 0x9F };
static const symbol s_1[] = { 's', 's' };
static const symbol s_2[] = { 'U' };
static const symbol s_3[] = { 'Y' };
static const symbol s_4[] = { 'y' };
static const symbol s_5[] = { 'u' };
static const symbol s_6[] = { 'a' };
static const symbol s_7[] = { 'o' };
static const symbol s_8[] = { 'n', 'i', 's' };
static const symbol s_9[] = { 'i', 'g' };
static const symbol s_10[] = { 'e', 'r' };
static const symbol s_11[] = { 'e', 'n' };

static int r_prelude(struct SN_env * z) {
    {   int c_test1 = z->c;
        while(1) {
            int c2 = z->c;
            {   int c3 = z->c;
                z->bra = z->c;
                if (!(eq_s(z, 2, s_0))) goto lab2;
                z->ket = z->c;
                {   int ret = slice_from_s(z, 2, s_1);
                    if (ret < 0) return ret;
                }
                goto lab1;
            lab2:
                z->c = c3;
                {   int ret = skip_utf8(z->p, z->c, z->l, 1);
                    if (ret < 0) goto lab0;
                    z->c = ret;
                }
            }
        lab1:
            continue;
        lab0:
            z->c = c2;
            break;
        }
        z->c = c_test1;
    }
    while(1) {
        int c4 = z->c;
        while(1) {
            int c5 = z->c;
            if (in_grouping_U(z, g_v, 97, 252, 0)) goto lab4;
            z->bra = z->c;
            {   int c6 = z->c;
                if (z->c == z->l || z->p[z->c] != 'u') goto lab6;
                z->c++;
                z->ket = z->c;
                if (in_grouping_U(z, g_v, 97, 252, 0)) goto lab6;
                {   int ret = slice_from_s(z, 1, s_2);
                    if (ret < 0) return ret;
                }
                goto lab5;
            lab6:
                z->c = c6;
                if (z->c == z->l || z->p[z->c] != 'y') goto lab4;
                z->c++;
                z->ket = z->c;
                if (in_grouping_U(z, g_v, 97, 252, 0)) goto lab4;
                {   int ret = slice_from_s(z, 1, s_3);
                    if (ret < 0) return ret;
                }
            }
        lab5:
            z->c = c5;
            break;
        lab4:
            z->c = c5;
            {   int ret = skip_utf8(z->p, z->c, z->l, 1);
                if (ret < 0) goto lab3;
                z->c = ret;
            }
        }
        continue;
    lab3:
        z->c = c4;
        break;
    }
    return 1;
}

static int r_mark_regions(struct SN_env * z) {
    z->I[2] = z->l;
    z->I[1] = z->l;
    {   int c_test1 = z->c;
        {   int ret = skip_utf8(z->p, z->c, z->l, 3);
            if (ret < 0) return 0;
            z->c = ret;
        }
        z->I[0] = z->c;
        z->c = c_test1;
    }
    {
        int ret = out_grouping_U(z, g_v, 97, 252, 1);
        if (ret < 0) return 0;
        z->c += ret;
    }
    {
        int ret = in_grouping_U(z, g_v, 97, 252, 1);
        if (ret < 0) return 0;
        z->c += ret;
    }
    z->I[2] = z->c;

    if (!(z->I[2] < z->I[0])) goto lab0;
    z->I[2] = z->I[0];
lab0:
    {
        int ret = out_grouping_U(z, g_v, 97, 252, 1);
        if (ret < 0) return 0;
        z->c += ret;
    }
    {
        int ret = in_grouping_U(z, g_v, 97, 252, 1);
        if (ret < 0) return 0;
        z->c += ret;
    }
    z->I[1] = z->c;
    return 1;
}

static int r_postlude(struct SN_env * z) {
    int among_var;
    while(1) {
        int c1 = z->c;
        z->bra = z->c;
        among_var = find_among(z, a_0, 6);
        if (!(among_var)) goto lab0;
        z->ket = z->c;
        switch (among_var) {
            case 1:
                {   int ret = slice_from_s(z, 1, s_4);
                    if (ret < 0) return ret;
                }
                break;
            case 2:
                {   int ret = slice_from_s(z, 1, s_5);
                    if (ret < 0) return ret;
                }
                break;
            case 3:
                {   int ret = slice_from_s(z, 1, s_6);
                    if (ret < 0) return ret;
                }
                break;
            case 4:
                {   int ret = slice_from_s(z, 1, s_7);
                    if (ret < 0) return ret;
                }
                break;
            case 5:
                {   int ret = skip_utf8(z->p, z->c, z->l, 1);
                    if (ret < 0) goto lab0;
                    z->c = ret;
                }
                break;
        }
        continue;
    lab0:
        z->c = c1;
        break;
    }
    return 1;
}

static int r_R1(struct SN_env * z) {
    if (!(z->I[2] <= z->c)) return 0;
    return 1;
}

static int r_R2(struct SN_env * z) {
    if (!(z->I[1] <= z->c)) return 0;
    return 1;
}

static int r_standard_suffix(struct SN_env * z) {
    int among_var;
    {   int m1 = z->l - z->c; (void)m1;
        z->ket = z->c;
        if (z->c <= z->lb || z->p[z->c - 1] >> 5 != 3 || !((811040 >> (z->p[z->c - 1] & 0x1f)) & 1)) goto lab0;
        among_var = find_among_b(z, a_1, 7);
        if (!(among_var)) goto lab0;
        z->bra = z->c;
        {   int ret = r_R1(z);
            if (ret == 0) goto lab0;
            if (ret < 0) return ret;
        }
        switch (among_var) {
            case 1:
                {   int ret = slice_del(z);
                    if (ret < 0) return ret;
                }
                break;
            case 2:
                {   int ret = slice_del(z);
                    if (ret < 0) return ret;
                }
                {   int m2 = z->l - z->c; (void)m2;
                    z->ket = z->c;
                    if (z->c <= z->lb || z->p[z->c - 1] != 's') { z->c = z->l - m2; goto lab1; }
                    z->c--;
                    z->bra = z->c;
                    if (!(eq_s_b(z, 3, s_8))) { z->c = z->l - m2; goto lab1; }
                    {   int ret = slice_del(z);
                        if (ret < 0) return ret;
                    }
                lab1:
                    ;
                }
                break;
            case 3:
                if (in_grouping_b_U(z, g_s_ending, 98, 116, 0)) goto lab0;
                {   int ret = slice_del(z);
                    if (ret < 0) return ret;
                }
                break;
        }
    lab0:
        z->c = z->l - m1;
    }
    {   int m3 = z->l - z->c; (void)m3;
        z->ket = z->c;
        if (z->c - 1 <= z->lb || z->p[z->c - 1] >> 5 != 3 || !((1327104 >> (z->p[z->c - 1] & 0x1f)) & 1)) goto lab2;
        among_var = find_among_b(z, a_2, 4);
        if (!(among_var)) goto lab2;
        z->bra = z->c;
        {   int ret = r_R1(z);
            if (ret == 0) goto lab2;
            if (ret < 0) return ret;
        }
        switch (among_var) {
            case 1:
                {   int ret = slice_del(z);
                    if (ret < 0) return ret;
                }
                break;
            case 2:
                if (in_grouping_b_U(z, g_st_ending, 98, 116, 0)) goto lab2;
                {   int ret = skip_b_utf8(z->p, z->c, z->lb, 3);
                    if (ret < 0) goto lab2;
                    z->c = ret;
                }
                {   int ret = slice_del(z);
                    if (ret < 0) return ret;
                }
                break;
        }
    lab2:
        z->c = z->l - m3;
    }
    {   int m4 = z->l - z->c; (void)m4;
        z->ket = z->c;
        if (z->c - 1 <= z->lb || z->p[z->c - 1] >> 5 != 3 || !((1051024 >> (z->p[z->c - 1] & 0x1f)) & 1)) goto lab3;
        among_var = find_among_b(z, a_4, 8);
        if (!(among_var)) goto lab3;
        z->bra = z->c;
        {   int ret = r_R2(z);
            if (ret == 0) goto lab3;
            if (ret < 0) return ret;
        }
        switch (among_var) {
            case 1:
                {   int ret = slice_del(z);
                    if (ret < 0) return ret;
                }
                {   int m5 = z->l - z->c; (void)m5;
                    z->ket = z->c;
                    if (!(eq_s_b(z, 2, s_9))) { z->c = z->l - m5; goto lab4; }
                    z->bra = z->c;
                    {   int m6 = z->l - z->c; (void)m6;
                        if (z->c <= z->lb || z->p[z->c - 1] != 'e') goto lab5;
                        z->c--;
                        { z->c = z->l - m5; goto lab4; }
                    lab5:
                        z->c = z->l - m6;
                    }
                    {   int ret = r_R2(z);
                        if (ret == 0) { z->c = z->l - m5; goto lab4; }
                        if (ret < 0) return ret;
                    }
                    {   int ret = slice_del(z);
                        if (ret < 0) return ret;
                    }
                lab4:
                    ;
                }
                break;
            case 2:
                {   int m7 = z->l - z->c; (void)m7;
                    if (z->c <= z->lb || z->p[z->c - 1] != 'e') goto lab6;
                    z->c--;
                    goto lab3;
                lab6:
                    z->c = z->l - m7;
                }
                {   int ret = slice_del(z);
                    if (ret < 0) return ret;
                }
                break;
            case 3:
                {   int ret = slice_del(z);
                    if (ret < 0) return ret;
                }
                {   int m8 = z->l - z->c; (void)m8;
                    z->ket = z->c;
                    {   int m9 = z->l - z->c; (void)m9;
                        if (!(eq_s_b(z, 2, s_10))) goto lab9;
                        goto lab8;
                    lab9:
                        z->c = z->l - m9;
                        if (!(eq_s_b(z, 2, s_11))) { z->c = z->l - m8; goto lab7; }
                    }
                lab8:
                    z->bra = z->c;
                    {   int ret = r_R1(z);
                        if (ret == 0) { z->c = z->l - m8; goto lab7; }
                        if (ret < 0) return ret;
                    }
                    {   int ret = slice_del(z);
                        if (ret < 0) return ret;
                    }
                lab7:
                    ;
                }
                break;
            case 4:
                {   int ret = slice_del(z);
                    if (ret < 0) return ret;
                }
                {   int m10 = z->l - z->c; (void)m10;
                    z->ket = z->c;
                    if (z->c - 1 <= z->lb || (z->p[z->c - 1] != 103 && z->p[z->c - 1] != 104)) { z->c = z->l - m10; goto lab10; }
                    if (!(find_among_b(z, a_3, 2))) { z->c = z->l - m10; goto lab10; }
                    z->bra = z->c;
                    {   int ret = r_R2(z);
                        if (ret == 0) { z->c = z->l - m10; goto lab10; }
                        if (ret < 0) return ret;
                    }
                    {   int ret = slice_del(z);
                        if (ret < 0) return ret;
                    }
                lab10:
                    ;
                }
                break;
        }
    lab3:
        z->c = z->l - m4;
    }
    return 1;
}

extern int german_UTF_8_stem(struct SN_env * z) {
    {   int c1 = z->c;
        {   int ret = r_prelude(z);
            if (ret < 0) return ret;
        }
        z->c = c1;
    }
    {   int c2 = z->c;
        {   int ret = r_mark_regions(z);
            if (ret < 0) return ret;
        }
        z->c = c2;
    }
    z->lb = z->c; z->c = z->l;


    {   int ret = r_standard_suffix(z);
        if (ret < 0) return ret;
    }
    z->c = z->lb;
    {   int c3 = z->c;
        {   int ret = r_postlude(z);
            if (ret < 0) return ret;
        }
        z->c = c3;
    }
    return 1;
}

extern struct SN_env * german_UTF_8_create_env(void) { return SN_create_env(0, 3); }

extern void german_UTF_8_close_env(struct SN_env * z) { SN_close_env(z, 0); }
